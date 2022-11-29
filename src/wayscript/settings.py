"""
Module for settings and configs
"""
import os

AUTH_ROUTE = "auth"
FILES_ROUTE = "files"
LAIRS_ROUTE = "lairs"
PROCESSES_ROUTE = "processes"
WEBHOOKS = "webhooks"
WORKSPACES_ROUTE = "workspaces"
WORKSPACE_INTEGRATIONS_ROUTE = "workspace-integrations"
TERMINAL_ROUTE = "terminal"


ROUTES = {
    "auth": {"refresh": f"{AUTH_ROUTE}/refresh"},
    "files": {"set_secret": f'{FILES_ROUTE}/lairs/$id/secrets'},
    "lairs": {"detail": f"{LAIRS_ROUTE}/$id"},
    "processes": {"detail_expanded": f"{PROCESSES_ROUTE}/$id/detail"},
    "terminal": {"output": f"{TERMINAL_ROUTE}/output"},
    "webhooks": {"http_trigger_response": f"{WEBHOOKS}/http-trigger/response/$id"},
    "workspaces": {
        "detail": f"{WORKSPACES_ROUTE}/$id",
        "user_application_key_detail": f"{WORKSPACES_ROUTE}/$id/users/self",
    },
    "workspace-integrations": {"detail": f"{WORKSPACE_INTEGRATIONS_ROUTE}/$id"},
}

# origin is scheme + domain + port. explanation: https://stackoverflow.com/a/37366696/4293004
WAYSCRIPT_ORIGIN = os.environ.get("WAYSCRIPT_ORIGIN", "https://api.wayscript.com")
