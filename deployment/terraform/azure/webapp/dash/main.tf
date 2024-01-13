# Use a pre-performed 'az login' to access Azure
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.86.0"
    }
  }

  # to specify a remote tfstate file in blob, create a backend.hcl file and
  # init terraform with `terraform init --backend-config=backend.hcl`
  # to run your tfstate locally, rather than in blob
  # init terraform with `terraform init --backend=false`
  backend "azurerm" {
    resource_group_name  = "<populate from a backend.hcl file>"
    storage_account_name = "<populate from a backend.hcl file>"
    container_name       = "tfstate"
    key                  = "dash-web-app.tfstate"
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id
}
