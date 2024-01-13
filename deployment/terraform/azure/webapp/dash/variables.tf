## main login
variable "subscription_id" {
  type        = string
  description = "Azure Subscription Id"
}

variable "tenant_id" {
  type        = string
  description = "Azure Tenant Id"
}

## generic params for all resources
variable "location" {
  type        = string
  default     = "uksouth"
  description = "Resource Group Location"
}

variable "creator" {
  type        = string
  description = "Entity or person creating the resources"
}

## resource group
variable "resource_group_name" {
  type        = string
  description = "Resource Group Name"
}

## web app
variable "web_app_pricing_plan" {
  type        = string
  default     = "F1"
  description = "Service plan SKU aka pricing plan"
}

variable "web_app_name" {
  type        = string
  description = "Web App Name - used in URI of web app (as the bottom level domain name) and various resource names (so no spaces or special chars)"
}

variable "web_app_cidrs_allow" {
  type        = list(string)
  default     = []
  description = "list of CIDRs for allowing access to web app"
}

variable "docker_image" {
  type        = string
  description = "name of the docker image to use in the web app - without tag"
}

variable "docker_tag" {
  type        = string
  default     = "latest"
  description = "tag of the docker image to use in the web app"
}

variable "docker_reg_url" {
  type        = string
  description = "docker registry to pull image from"
}

variable "docker_reg_username" {
  type        = string
  description = "username to use for docker login into docker registry"
}

variable "docker_reg_password" {
  type        = string
  description = "password to use for docker login into docker registry"
}

variable "healthcheck_endpoint" {
  type        = string
  description = "endpoint on app to use for healthcheck - starts with /"
}

variable "key_vault_ips_allow" {
  type        = list(string)
  default     = []
  description = "list of ips and/or cidrs for allowing access to key vault"
}

variable "key_vault_vnet_subnet_ids_allow" {
  type        = list(string)
  default     = []
  description = "list of virtual network subnet ids for allowing access to key vault"
}

variable "key_vault_secrets" {
  type        = map(string)
  default     = {}
  description = "Secrets as name:value to put in key vault"
}

variable "app_env_var_secrets_mount" {
  type        = map(string)
  default     = {}
  description = "environment variables mounted as secrets from the key vault as env_var:secret_name"
}
