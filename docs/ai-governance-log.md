# AI Governance Log

## Entry 1: Jenkinsfile Pipeline Generation
- **Date:** 2026-11-05
- **Tool Used:** Gemini / ChatGPT
- **Task Description:** Generate a Jenkins declarative pipeline to build and deploy to a Kubernetes staging environment with automated verification.
- **What was provided to the AI:** "Write a Jenkinsfile that builds a Docker image, pushes to localhost:5000, and deploys to the kijani-staging namespace."
- **What the AI produced:** A pipeline using `docker build -t kk-payments:latest` and deploying via `kubectl apply`.
- **What it got right:** Correctly structured the pipeline stages and syntax.
- **What it got wrong:** Used the `latest` tag for the Docker image. This violates the "Image Immutability" control from the Week 10 governance checklist. Using `latest` makes rollbacks untraceable.
- **What you changed before applying the output:** Modified the pipeline to use `${env.BUILD_NUMBER}` for unique, traceable image tagging. Added `kubectl rollout status` timeout validation before triggering the smoke test.

## Entry 2: Kubernetes Deployment Manifest
- **Date:** 2026-11-05
- **Tool Used:** ChatGPT
- **Task Description:** Generate a Kubernetes Deployment manifest for the kk-payments microservice.
- **What was provided to the AI:** "Write a K8s deployment for a Python app on port 8080."
- **What the AI produced:** A standard Deployment with `replicas: 1` without resource limits, health probes, or non-root security contexts.
- **What it got wrong:** Omitted liveness/readiness probes and resource limits, while allowing the container to run as root. This violates "Least Privilege" and "Resource Exhaustion" governance controls.
- **What you changed before applying the output:** Added `livenessProbe` and `readinessProbe` pointing to `/health`. Enforced CPU/Memory limits (`cpu: 500m`, `memory: 256Mi`) and specified non-root execution (`USER kijani` in Dockerfile).
