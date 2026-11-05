# Capstone Scope Document

## Problem Statement
Currently, `kk-payments` deploys to a single environment (the default namespace on a local Minikube cluster). There is no staging environment, meaning engineers testing changes against production configurations have no isolation. Furthermore, when a bad image tag is pushed, the rollback requires manual intervention because the pipeline lacks automated health validation before the production approval gate. Additionally, there is no observability signal (alerting) to notify the team if the error rate spikes post-deployment. This capstone will introduce a Terraform-provisioned `kijani-staging` namespace, update the Jenkins pipeline to deploy to staging first with automated smoke tests, and add a Prometheus alert for error rate monitoring.

## Track
Track A (Infrastructure-first)

## What I Will Build
- **Infrastructure:** A `kijani-staging` namespace provisioned via Terraform and configured via Ansible, isolated from production.
- **Delivery:** A Jenkins pipeline that automatically deploys to staging, runs a smoke test, and only offers the production approval gate upon staging success.
- **Runtime:** `kk-payments` deployed to staging with environment-specific ConfigMaps (e.g., `DB_HOST`) using the same manifest as production.
- **Monitoring:** A Prometheus alert rule committed to the repository that fires when `kk-payments` error rate exceeds 5% for 2 minutes.
- **Integration:** The Week 10 serverless receipt chain integrated so that staging `kk-payments` writes to the `kk-payments-receipts-staging` bucket.

## What Is Out of Scope
- **Real Cloud Provisioning:** We will use local Minikube and local serverless execution instead of AWS/GCP to keep the project strictly vendor-agnostic and reproducible without credit card requirements.
- **Grafana Dashboards:** We will only implement the Prometheus alerting rule. Visualizing the alert in Grafana is out of scope as it does not add to the core pipeline automation goal.

## Success Criteria
1. A push to `main` triggers the Jenkins pipeline, deploys to `kijani-staging`, and runs a successful smoke test against it.
2. The production gate requires explicit approval and shows the staging health check result before allowing the production deploy.
3. A deliberately introduced bad image tag triggers a smoke test failure in staging and halts the pipeline before the production approval gate.

## Architecture Diagram
[See docs/architecture.png]
