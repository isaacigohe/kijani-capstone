# Capstone Reflection

## 1. What did you get wrong?
Initially, I designed the Jenkins pipeline to push the Docker image using the `latest` tag. I assumed that because the pipeline ran sequentially, the cluster would always pull the newest image. I was wrong. During a simulated rollback test, I realized that using `latest` makes it impossible to trace which version of the code is running in production, and it breaks Kubernetes' ability to roll back to a known good state. If I did this again, I would implement the `${env.BUILD_NUMBER}` tag from day one and enforce it as a strict rule in the Jenkinsfile, as image immutability is a non-negotiable production standard.

## 2. What is the most important thing you learned?
The most important concept I learned was the critical difference between Infrastructure Provisioning and Configuration Management, introduced in Week 4. Before this capstone, I viewed Terraform and Ansible as interchangeable tools for setting up servers. Building Track A taught me that Terraform creates the "house" (the namespace and its resources), while Ansible puts the "furniture" inside (the environment-specific ConfigMaps). Understanding this seam changed how I think about software delivery: it allowed me to use the exact same Kubernetes Deployment manifest for both staging and production, injecting only the environment variables at runtime via Ansible. This DRY (Don't Repeat Yourself) approach eliminates configuration drift.

## 3. What would a second pass look like?
If I had two more weeks, I would change three specific things:
- **Move to a Managed Cloud:** I would migrate from local Minikube to AWS EKS, replacing the local registry with Amazon ECR.
- **Secrets Management:** I would replace the plaintext Ansible ConfigMaps with HashiCorp Vault or AWS Secrets Manager to ensure database credentials are encrypted at rest and in transit.
- **Full Observability Stack:** I would deploy the Prometheus Alertmanager using a Helm chart, alongside a Grafana dashboard, to visualize the 5% error rate threshold firing in real-time rather than just keeping the rule as a static file.
