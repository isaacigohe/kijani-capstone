# Capstone Test Plan

- **Reviewer:** Alex (Peer Reviewer)
- **Objective:** Systematically validate Track A multi-environment setup and recovery logic.

## Test Cases
1. **Fresh Setup:** Clone repository, run Terraform to provision `kijani-staging`, apply Ansible playbook for ConfigMap injection.
2. **Happy Path:** Trigger Jenkins pipeline $\rightarrow$ verify staging deployment $\rightarrow$ pass smoke test $\rightarrow$ confirm production approval gate.
3. **Failure Path:** Inject invalid image tag (`v999-bad`) $\rightarrow$ verify rollout timeout/smoke test failure halts pipeline before production.
4. **AI Governance:** Audit `docs/ai-governance-log.md` for proper 8-field structure and negative feedback logs.
