# Peer Feedback Log

## Issue 1: Missing Docker Environment Context Step in Setup
- **Issue:** Setup instructions failed at `docker build` because the shell environment was not pointed to Minikube's internal daemon (`eval $(minikube docker-env)`), causing `ErrImagePull`.
- **Severity:** Blocks Setup.
- **Resolution:** Updated README setup steps to include explicit `eval $(minikube docker-env)` step.
- **Evidence:** Closed via GitHub Issue #1.

## Issue 2: Clarification of Out-of-Scope Criteria
- **Issue:** Peer reviewer requested justification for omitting cloud provider deployment.
- **Severity:** Minor Documentation Improvement.
- **Resolution:** Explicitly detailed in `docs/scope.md` that local Minikube execution is used to guarantee vendor-agnostic, zero-cost reproducibility.
- **Evidence:** Updated `docs/scope.md`.

## Issue 3: Pipeline Smoke Test Error Output
- **Issue:** Recommended printing pod status upon smoke test failure to speed up live debugging.
- **Severity:** Enhancement.
- **Resolution:** Added pod status check block to Jenkins pipeline failure handler.
- **Evidence:** Updated `Jenkinsfile`.
