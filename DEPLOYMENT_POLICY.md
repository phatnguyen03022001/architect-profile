# DEPLOYMENT POLICY

This file records the operator-specific deployment default for future projects.

## Vercel

For every project connected to Vercel, Git pushes must **not** automatically deploy the production branch.

Default production policy:

```text
push / merge to production branch
→ update repository truth only
→ NO automatic Vercel production deployment

operator explicitly requests deployment
→ deploy / promote production
```

For repositories whose production branch is `main`, ensure the effective Vercel project configuration includes:

```json
{
  "git": {
    "deploymentEnabled": {
      "main": false
    }
  }
}
```

If `vercel.json` already exists, merge this policy into the existing configuration rather than replacing unrelated settings.

The configuration must live at the actual Vercel Project Root. For monorepos or projects configured with a subdirectory root, place or merge the effective configuration where Vercel reads it for that project.

If the production branch is not `main`, disable automatic deployment for the actual production branch instead.

Preview-branch behavior is independent. Do not disable previews unless the operator explicitly requests that broader policy.

## Project onboarding rule

When a new repository/project is connected to Vercel, treat manual production deployment as the default before normal development continues:

```text
identify Vercel Project Root
→ identify production branch
→ preserve existing Vercel settings
→ disable Git-triggered deployment for the production branch
→ verify the effective repository configuration
```

Do not rely on Vercel account/team defaults for this behavior; enforce it per project.

This is an operator preference, not generic engineering governance.
