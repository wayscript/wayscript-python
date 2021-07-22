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


WAYSCRIPT_HOST = os.environ.get("WAYSCRIPT_HOST", "api.wayscript.com")
WAYSCRIPT_VERSION = os.environ.get("WAYSCRIPT_VERSION", "v0")
