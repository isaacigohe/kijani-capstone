terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "staging" {
  metadata {
    name = var.namespace_name
    labels = {
      environment = "staging"
      managed_by  = "terraform"
    }
  }
}
