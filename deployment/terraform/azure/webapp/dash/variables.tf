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
  description = "Web App Name - used in URI of web app"
}

variable docker_image {
  type = string
}

variable docker_tag {
  type = string
  default = "latest"
}

variable "docker_reg_url" {
  type = string
}

variable "docker_reg_username" {
  type = string
}

variable "docker_reg_password" {
  type = string
}