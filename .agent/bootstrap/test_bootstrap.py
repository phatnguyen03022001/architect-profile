#!/usr/bin/env python3
import copy
import base64
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agent" / "bootstrap"))

import validate  # noqa: E402

VALIDATOR = ROOT / ".agent" / "bootstrap" / "validate.py"
PROFILE_REVISION = "707acfea1f749591621751785b87ae792355a0eb"


class BootstrapContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bootstrap, self.lock = validate.load_contract(ROOT)

    def test_validator_accepts_canonical_bootstrap(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_capability_entrypoint_fails_closed(self) -> None:
        bootstrap = copy.deepcopy(self.bootstrap)
        bootstrap["capability_routes"].append(copy.deepcopy(bootstrap["capability_routes"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate capability"):
            validate.validate_contract(bootstrap, self.lock)

    def resolved_routes(self):
        resolved = {}
        for owner, entry in self.lock["repositories"].items():
            resolved[owner] = {"revision": entry["revision"], "paths": set()}
        for route in self.bootstrap["capability_routes"]:
            resolved[route["owner"]]["paths"].add(route["path"])
        return resolved

    def resolved_routes_with_router(self, router: str) -> dict:
        resolved = self.resolved_routes()
        resolved["agent-skills"]["paths"].add(".agent/case-router.yaml")
        resolved["agent-skills"]["contents"] = {".agent/case-router.yaml": router}
        return resolved

    def test_unresolvable_locked_revision_fails_closed(self) -> None:
        resolved = self.resolved_routes()
        del resolved["agent-runtime"]
        with self.assertRaisesRegex(ValueError, "unresolvable locked revision"):
            validate.validate_resolution(self.bootstrap, self.lock, resolved)

    def test_missing_routed_path_fails_closed(self) -> None:
        resolved = self.resolved_routes()
        resolved["agent-skills"]["paths"].remove("executor/SKILL.md")
        with self.assertRaisesRegex(ValueError, "missing routed path"):
            validate.validate_resolution(self.bootstrap, self.lock, resolved)

    def test_missing_case_router_path_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "missing Case Router path"):
            validate.validate_resolution(self.bootstrap, self.lock, self.resolved_routes())

    def test_malformed_case_router_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed Case Router"):
            validate.validate_resolution(
                self.bootstrap,
                self.lock,
                self.resolved_routes_with_router("cases:\n  - id: EXECUTE\n    capabilities: executor\n"),
            )

    def test_case_router_rejects_unadmitted_case(self) -> None:
        with self.assertRaisesRegex(ValueError, "unauthorized Case Router semantics"):
            validate.validate_resolution(
                self.bootstrap,
                self.lock,
                self.resolved_routes_with_router(
                    "cases:\n  - id: REVIEW\n    capabilities:\n      - executor\n"
                ),
            )

    def test_case_router_rejects_lifecycle_or_dimension_fields(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed Case Router"):
            validate.validate_resolution(
                self.bootstrap,
                self.lock,
                self.resolved_routes_with_router(
                    "cases:\n  - id: EXECUTE\n    capabilities:\n      - executor\n    state: READY\n"
                ),
            )

    def test_unknown_case_selection_fails_closed(self) -> None:
        router = {"cases": [{"id": "EXECUTE", "capabilities": ["executor"]}]}
        with self.assertRaisesRegex(ValueError, "unknown case"):
            validate.select_case_capability_routes(self.bootstrap, router, "VERIFY")

    def test_mutable_ref_in_lock_fails_closed(self) -> None:
        lock = copy.deepcopy(self.lock)
        lock["repositories"]["agent-skills"]["revision"] = "main"
        with self.assertRaisesRegex(ValueError, "invalid immutable revision"):
            validate.validate_contract(self.bootstrap, lock)

    def test_remote_resolution_loads_router_bytes_from_the_locked_tree_blob(self) -> None:
        router = "cases:\n  - id: EXECUTE\n    capabilities:\n      - executor\n"
        router_blob = "c" * 40
        routes_by_owner = {owner: [] for owner in self.lock["repositories"]}
        for route in self.bootstrap["capability_routes"]:
            routes_by_owner[route["owner"]].append(route["path"])

        def fake_github_json(url: str) -> dict:
            if "/git/commits/" in url:
                revision = url.rsplit("/", 1)[1]
                owner = next(
                    owner
                    for owner, entry in self.lock["repositories"].items()
                    if entry["revision"] == revision
                )
                return {"sha": revision, "tree": {"sha": f"{owner}-tree"}}
            if "/git/trees/" in url:
                owner = next(owner for owner in routes_by_owner if f"/{owner}-tree?" in url)
                paths = routes_by_owner[owner]
                entries = [{"path": path, "sha": f"{owner}-{index}"} for index, path in enumerate(paths)]
                if owner == "agent-skills":
                    entries.append({"path": ".agent/case-router.yaml", "sha": router_blob})
                return {"truncated": False, "tree": entries}
            if url.endswith(f"/git/blobs/{router_blob}"):
                return {"encoding": "base64", "content": base64.b64encode(router.encode()).decode()}
            self.fail(f"unexpected GitHub request: {url}")

        with patch.object(validate, "_github_json", side_effect=fake_github_json):
            resolved = validate.resolve_remote(self.lock)
        self.assertEqual(resolved["agent-skills"]["contents"][".agent/case-router.yaml"], router)

    def test_unknown_execution_surface_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown execution surface"):
            validate.normalize_surface(self.bootstrap, "CHATGPT", "CLOUD")

    def test_ambiguous_execution_surface_fails_closed(self) -> None:
        bootstrap = copy.deepcopy(self.bootstrap)
        bootstrap["execution_surfaces"][2]["controller"] = "CHATGPT"
        bootstrap["execution_surfaces"][2]["location"] = "LOCAL"
        with self.assertRaisesRegex(ValueError, "ambiguous execution surface"):
            validate.normalize_surface(bootstrap, "CHATGPT", "LOCAL")

    def test_agent_runtime_cannot_be_execution_mode(self) -> None:
        bootstrap = copy.deepcopy(self.bootstrap)
        bootstrap["execution_surfaces"][0]["id"] = "AGENT_RUNTIME"
        with self.assertRaises(ValueError):
            validate.validate_contract(bootstrap, self.lock)

    def test_execution_routes_match_opm02_exactly(self) -> None:
        self.assertEqual(
            {
                surface["id"]: (surface["model"], surface["effort"])
                for surface in self.bootstrap["execution_surfaces"]
            },
            {
                "CHATGPT_GITHUB": ("GPT-5.6 Sol", "HIGH"),
                "CHATGPT_LOCAL": ("GPT-5.6 Sol", "HIGH"),
                "CODEX_CLOUD": ("LUNA", "XHIGH"),
                "CODEX_LOCAL": ("LUNA", "XHIGH"),
            },
        )

    def test_unauthorized_model_or_effort_fails_closed(self) -> None:
        cases = (
            (1, "model", "OTHER"),
            (1, "effort", "LOW"),
            (2, "model", "OTHER"),
            (2, "effort", "MEDIUM"),
            (3, "effort", "HIGH"),
        )
        for surface_index, field, value in cases:
            with self.subTest(surface_index=surface_index, field=field, value=value):
                bootstrap = copy.deepcopy(self.bootstrap)
                bootstrap["execution_surfaces"][surface_index][field] = value
                with self.assertRaisesRegex(ValueError, "unauthorized execution routing"):
                    validate.validate_contract(bootstrap, self.lock)

    def test_p1_lock_matches_task_authority_exactly(self) -> None:
        self.assertEqual(
            self.lock["repositories"],
            {
                "agent-skills": {
                    "repository": "phatnguyen03022001/agent-skills",
                    "revision": "ed8d9fb35bb8b052530ca879e68a227d77e4a8a6",
                },
                "agent-standards": {
                    "repository": "phatnguyen03022001/agent-standards",
                    "revision": "3f4950f280a3a35fee81471d4b83715fa72cf9ee",
                },
                "agent-documents": {
                    "repository": "phatnguyen03022001/agent-documents",
                    "revision": "6918f46282f4a92bbc61071444a5ff5dab30ddc9",
                },
                "agent-runtime": {
                    "repository": "phatnguyen03022001/agent-runtime",
                    "revision": "c49d777efa09db7f6c51bd8d8616db4623499fb8",
                },
            },
        )

    def test_all_four_surfaces_normalize_uniquely(self) -> None:
        expected = {
            ("CHATGPT", "GITHUB"): "CHATGPT_GITHUB",
            ("CHATGPT", "LOCAL"): "CHATGPT_LOCAL",
            ("CODEX", "CLOUD"): "CODEX_CLOUD",
            ("CODEX", "LOCAL"): "CODEX_LOCAL",
        }
        for key, surface_id in expected.items():
            with self.subTest(controller=key[0], location=key[1]):
                self.assertEqual(validate.normalize_surface(self.bootstrap, *key)["id"], surface_id)

    def test_authority_identity_uses_profile_commit_without_self_pin(self) -> None:
        identity = self.bootstrap["authority_set_identity"]
        self.assertEqual(identity["source"], "ARCHITECT_PROFILE_COMMIT")
        self.assertFalse(identity["self_pin"])
        self.assertEqual(identity["evolution_ref"], "dev")
        self.assertEqual(identity["activation_ref"], "main")
        self.assertEqual(identity["rollback"], "FORWARD_ACTIVATION_COMMIT")
        self.assertNotIn("architect-profile", self.lock["repositories"])

    def test_target_binding_requires_explicit_current_identity(self) -> None:
        self.assertEqual(
            self.bootstrap["target_binding"],
            {
                "source": "EXPLICIT_CURRENT_REQUEST_OR_EXACT_ACTIVE_BINDING",
                "fresh_github_resolution_required": True,
                "unresolved_action": "ASK_OPERATOR",
                "forbidden_inference_sources": [
                    "STALE_CHAT_HISTORY",
                    "MEMORY",
                    "CWD",
                    "LOCAL_DIRECTORY_NAME",
                ],
                "required_fields": [
                    "repository",
                    "branch",
                    "task_path",
                    "task_revision",
                    "base_head",
                    "phase",
                ],
            },
        )

    def test_prompt_is_rendered_only_from_canonical_locator_inputs(self) -> None:
        inputs = {
            "repository": "owner/repo",
            "branch": "dev",
            "task_path": ".agent/tasks/TASK-0001/task.yaml",
            "task_revision": 2,
            "base_head": "a" * 40,
            "phase": "EXECUTION",
            "surface": "CHATGPT_LOCAL",
        }
        prompt = validate.render_task_prompt(self.bootstrap, inputs)
        self.assertEqual(
            prompt,
            "Target: owner/repo\n"
            "Branch: dev\n"
            "Task: .agent/tasks/TASK-0001/task.yaml\n"
            "Task revision: 2\n"
            f"Exact base HEAD: {'a' * 40}\n"
            "Phase: EXECUTION\n"
            "Execution surface: CHATGPT_LOCAL\n"
            "Resolve the canonical task at the exact base and obey it exactly. "
            "Communicate with the operator in Vietnamese. Persist repository artifacts in English.",
        )

    def test_task_launch_fixtures_render_from_surface_contract(self) -> None:
        fixtures = self.bootstrap["task_launch"]["fixtures"]
        for surface_id, expected in fixtures.items():
            with self.subTest(surface=surface_id):
                self.assertEqual(validate.render_task_launch(self.bootstrap, surface_id, "NEW"), expected)

    def test_fresh_context_reconstruction_is_bounded_and_chat_free(self) -> None:
        target_locator = {
            "repository": "owner/repo",
            "branch": "dev",
            "task_path": ".agent/tasks/TASK-0001/task.yaml",
            "task_revision": 2,
            "base_head": "a" * 40,
            "phase": "EXECUTION",
        }
        result = validate.reconstruct_context(
            root=ROOT,
            profile_revision=PROFILE_REVISION,
            target_locator=target_locator,
            required_capabilities=["executor", "verification"],
            controller="CHATGPT",
            location="LOCAL",
        )
        self.assertEqual(result["authority_set_identity"], PROFILE_REVISION)
        self.assertEqual(result["target_binding"], target_locator)
        self.assertEqual(result["surface"]["id"], "CHATGPT_LOCAL")
        self.assertEqual(result["surface"]["transport"], "AGENT_RUNTIME")
        self.assertEqual(
            [route["capability"] for route in result["capability_routes"]],
            ["executor", "verification"],
        )
        self.assertNotIn("chat_history", result)
        self.assertEqual(
            result["repository_contract"],
            {
                "repository": "phatnguyen03022001/architect-profile",
                "topology": "DEV_MAIN",
                "working_ref": "dev",
                "stable_ref": "main",
                "local_policy": "MANAGED_MIRROR",
            },
        )

    def test_fresh_context_reconstruction_exposes_the_pre_router_locator(self) -> None:
        target_locator = {
            "repository": "owner/repo",
            "branch": "dev",
            "task_path": ".agent/tasks/TASK-0001/task.yaml",
            "task_revision": 2,
            "base_head": "a" * 40,
            "phase": "EXECUTION",
        }
        result = validate.reconstruct_context(
            root=ROOT,
            profile_revision=PROFILE_REVISION,
            target_locator=target_locator,
            required_capabilities=["executor"],
            controller="CODEX",
            location="LOCAL",
        )
        self.assertIn("case_router", result)

    def test_execution_reconstruction_resolves_execute_without_support_preload(self) -> None:
        reconstruct = getattr(validate, "reconstruct_execution_context", None)
        self.assertTrue(callable(reconstruct))
        if not callable(reconstruct):
            return
        target_locator = {
            "repository": "phatnguyen03022001/architect-profile",
            "branch": "dev",
            "task_path": ".agent/tasks/TASK-0018/task.yaml",
            "task_revision": 1,
            "base_head": "a" * 40,
            "phase": "EXECUTION",
        }
        router = "cases:\n  - id: EXECUTE\n    capabilities:\n      - executor\n"
        resolved = {
            "agent-skills": {
                "revision": self.lock["repositories"]["agent-skills"]["revision"],
                "paths": {".agent/case-router.yaml", "executor/SKILL.md"},
                "contents": {".agent/case-router.yaml": router},
            }
        }
        result = reconstruct(ROOT, "b" * 40, target_locator, "EXECUTE", resolved)
        self.assertEqual(
            result["bootstrap_trace"],
            ["PROFILE_REVISION", "AUTHORITY_LOCK", "CASE_ROUTER", "CASE", "CAPABILITY_ROUTE", "CANONICAL_ARTIFACT"],
        )
        self.assertEqual(result["case"], "EXECUTE")
        self.assertEqual(result["case_router"], {"cases": [{"id": "EXECUTE", "capabilities": ["executor"]}]})
        self.assertEqual(
            result["canonical_artifacts"],
            [
                {
                    "capability": "executor",
                    "repository": "phatnguyen03022001/agent-skills",
                    "revision": "ed8d9fb35bb8b052530ca879e68a227d77e4a8a6",
                    "path": "executor/SKILL.md",
                }
            ],
        )
        self.assertNotIn("chat_history", result)
        self.assertNotIn("cwd", result)

    def test_fresh_context_reconstruction_requires_exact_target_locator(self) -> None:
        with self.assertRaisesRegex(ValueError, "target locator"):
            validate.reconstruct_context(
                root=ROOT,
                profile_revision=PROFILE_REVISION,
                target_locator={
                    "branch": "dev",
                    "task_path": ".agent/tasks/TASK-0001/task.yaml",
                    "task_revision": 2,
                    "base_head": "a" * 40,
                    "phase": "EXECUTION",
                },
                required_capabilities=["executor"],
                controller="CHATGPT",
                location="LOCAL",
            )

    def test_generic_role_authority_remains_owned_by_agent_skills(self) -> None:
        routes = {route["capability"]: route for route in self.bootstrap["capability_routes"]}
        for capability in ("architect", "executor", "task_protocol"):
            with self.subTest(capability=capability):
                self.assertEqual(routes[capability]["owner"], "agent-skills")
        for forbidden_key in ("roles", "role_engine", "review_roles", "executor_specializations"):
            self.assertNotIn(forbidden_key, self.bootstrap)


if __name__ == "__main__":
    unittest.main(verbosity=2)
