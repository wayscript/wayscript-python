"""
Module for settings and configs
"""
import os


PROCESSES_ROUTE = "processes"
LAIRS_ROUTE = "lairs"
WORKSPACES_ROUTE = "workspaces"


ROUTES = {
    "lairs": {"detail": f"{LAIRS_ROUTE}/$id"},
    "processes": { "detail_expanded": f"{PROCESSES_ROUTE}/$id/detail"},
    "workspaces": {"detail": f"{WORKSPACES_ROUTE}/$id"},
}

# origin is scheme + domain + port. explanation: https://stackoverflow.com/a/37366696/4293004
WAYSCRIPT_ORIGIN = os.environ.get("WAYSCRIPT_ORIGIN", "https://api.wayscript.com")
