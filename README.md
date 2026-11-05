# KijaniKiosk Capstone - Track A (Infrastructure-First)

## What is this?
This repository contains the production-approaching infrastructure for KijaniKiosk. It provisions an isolated `kijani-staging` namespace via Terraform, injects environment configurations via Ansible, and deploys the `kk-payments` service through a Jenkins CI/CD pipeline featuring automated smoke tests and a production approval gate.

## Architecture
![Architecture Diagram](docs/architecture.png)

- **Terraform:** Provisions the `kijani-staging` namespace declaratively.
- **Ansible:** Injects the `kk-payments-config` ConfigMap with staging parameters.
- **Jenkins:** Automates build, staging deployment, smoke testing, and production promotion.
- **Prometheus:** Monitors service error rates and alerts on failures.

## Prerequisites
- Ubuntu / WSL2
- Docker (v29+)
- Minikube (v1.37+)
- Kubectl (v1.37+)
- Terraform (v1.16+)
- Ansible (v2.21+)

## Setup
1. **Start Minikube Cluster:**
   \`\`\`bash
   minikube start --driver=docker
   \`\`\`
2. **Point Shell Context to Minikube Docker Daemon (Fix for Issue #1):**
   \`\`\`bash
   eval \$(minikube docker-env)
   \`\`\`
3. **Provision Infrastructure (Terraform):**
   \`\`\`bash
   cd terraform && terraform init && terraform apply -auto-approve && cd ..
   \`\`\`
4. **Configure Staging Environment (Ansible):**
   \`\`\`bash
   cd ansible && ansible-playbook -i inventory/hosts.ini playbook.yml && cd ..
   \`\`\`
5. **Build Application Image:**
   \`\`\`bash
   docker build -t localhost:5000/kk-payments:v1 ./app
   \`\`\`
6. **Deploy Manifests to Staging:**
   \`\`\`bash
   kubectl apply -f k8s/ -n kijani-staging
   \`\`\`

## How to Run the Pipeline
1. Open Jenkins and create a new Pipeline project pointing to this GitHub repository.
2. Trigger the job. The pipeline will build the container, deploy to `kijani-staging`, execute the smoke test, and pause at the **Approval for Production** gate.
3. Approve the prompt to complete deployment to the `default` namespace.

## How to Verify it Works
1. **Inspect Staging Pods:**
   \`\`\`bash
   kubectl get pods -n kijani-staging
   \`\`\`
2. **Verify Structured Log Output:**
   \`\`\`bash
   kubectl logs -l app=kk-payments -n kijani-staging --tail=10
   \`\`\`
   *(Logs will display structured JSON with `"environment": "staging"`).*

## Known Limitations
- **Local Minikube Execution:** Designed for local evaluation to ensure zero vendor lock-in or cloud cost overhead.
- **Alerting:** Alert rules are committed in `monitoring/alerts.yml`, but rely on an external running Prometheus instance to process triggers.
