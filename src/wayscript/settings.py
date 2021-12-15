"""
Module for settings and configs
"""
import os

AUTH_ROUTE = "auth"
PROCESSES_ROUTE = "processes"
LAIRS_ROUTE = "lairs"
WEBHOOKS = "webhooks"
WORKSPACES_ROUTE = "workspaces"
WORKSPACE_INTEGRATIONS_ROUTE = "workspace-integrations"



ROUTES = {
    "auth": {"refresh": f"{AUTH_ROUTE}/refresh"},
    "lairs": {"detail": f"{LAIRS_ROUTE}/$id"},
    "processes": { "detail_expanded": f"{PROCESSES_ROUTE}/$id/detail"},
    "webhooks": {"http_trigger_response": f"{WEBHOOKS}/http-trigger/response/$id"},
    "workspaces": {
        "detail": f"{WORKSPACES_ROUTE}/$id",
        "user_application_key_detail": f"{WORKSPACES_ROUTE}/$id/users/self",
        },
    "workspace-integrations": {"detail": f"{WORKSPACE_INTEGRATIONS_ROUTE}/$id"},
}

# origin is scheme + domain + port. explanation: https://stackoverflow.com/a/37366696/4293004
WAYSCRIPT_ORIGIN = os.environ.get("WAYSCRIPT_ORIGIN", "https://api.wayscript.com")
