# Use a pre-performed 'az login' to access Azure
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.86.0"
    }
  }

  # remove this backend block to save your tfstate locally, rather than in blob
  backend "azurerm" {
      # these values need to be hard-coded since they are read at the terraform init stage
      # but may well be different for your setup
      resource_group_name  = "made-by-terraform-group"
      storage_account_name = "madebyterraformwithrg"
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
