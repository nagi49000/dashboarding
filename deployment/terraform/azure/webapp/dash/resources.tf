locals {
  common_tags = {
    appgroup = var.web_app_name
    creator  = var.creator
  }
}

resource "azurerm_service_plan" "web_app_service_plan" {
  name                = "${var.web_app_name}-service-plan"
  resource_group_name = var.resource_group_name
  location            = var.location
  os_type             = "Linux"
  sku_name            = var.web_app_pricing_plan
  tags = merge(
    local.common_tags,
    {
      "name" : "${var.web_app_name}-service-plan"
    }
  )
}

resource "azurerm_linux_web_app" "web_app" {
  name                = var.web_app_name
  resource_group_name = var.resource_group_name
  location            = var.location
  service_plan_id     = azurerm_service_plan.web_app_service_plan.id

  tags = merge(
    local.common_tags,
    {
      "name" = var.web_app_name
    }
  )

  site_config {
    always_on         = false
    health_check_path = var.healthcheck_endpoint
    application_stack {
      docker_image_name        = "${var.docker_image}:${var.docker_tag}"
      docker_registry_url      = var.docker_reg_url
      docker_registry_username = var.docker_reg_username
      docker_registry_password = var.docker_reg_password
    }
  }

  logs {
    application_logs {
      file_system_level = "Information"
    }
    http_logs {
      file_system {
        retention_in_mb   = 35
        retention_in_days = 7
      }
    }
  }

  # no idea why WEBSITES_ENABLE_APP_SERVICE_STORAGE is needed, but inside the
  # container Python module import errors occur without it
  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
  }
}