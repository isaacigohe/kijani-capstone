output "namespace" {
  description = "The provisioned staging namespace"
  value       = kubernetes_namespace.staging.metadata[0].name
}
