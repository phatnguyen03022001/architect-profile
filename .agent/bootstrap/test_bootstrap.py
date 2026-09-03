#!/usr/bin/env python3
import copy
import subprocess
import sys
import unittest
from pathlib import Path

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

    def test_unauthorized_model_or_effort_fails_closed(self) -> None:
        for field, value in (("model", "OTHER"), ("effort", "LOW")):
            with self.subTest(field=field):
                bootstrap = copy.deepcopy(self.bootstrap)
                bootstrap["execution_surfaces"][1][field] = value
                with self.assertRaisesRegex(ValueError, "unauthorized execution routing"):
                    validate.validate_contract(bootstrap, self.lock)

    def test_p1_lock_matches_task_authority_exactly(self) -> None:
        self.assertEqual(
            self.lock["repositories"],
            {
                "agent-skills": {
                    "repository": "phatnguyen03022001/agent-skills",
                    "revision": "337c0be6618090e704b345b1bf93df488a4985af",
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
                    "revision": "9d5320d5afbc9aff20834801bfd6695b27cf2a0e",
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

    def test_target_binding_comes_from_canonical_task_or_handoff(self) -> None:
        binding = self.bootstrap["target_binding"]
        self.assertEqual(binding["source"], "CANONICAL_TASK_OR_HANDOFF")
        self.assertEqual(
            binding["required_fields"],
            ["repository", "branch", "task_path", "task_revision", "base_head", "phase"],
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
        result = validate.reconstruct_context(
            root=ROOT,
            profile_revision=PROFILE_REVISION,
            required_capabilities=["executor", "verification"],
            controller="CHATGPT",
            location="LOCAL",
        )
        self.assertEqual(result["authority_set_identity"], PROFILE_REVISION)
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
