import os
import string

import requests

from . import settings


def get_process_execution_user_token():
    """Return the auth token of the user this process is executing on behalf of"""
    token = os.environ["WAYSCRIPT_EXECUTION_USER_TOKEN"]
    return token


def get_process_uuid():
    """Return uuid of current container execution"""
    process_uuid = os.environ["WAYSCRIPT_PROCESS_UUID"]
    return process_uuid


class WayScriptClient:

    def __init__(self, *args, **kwargs):
        """Init a wayscript client"""
        self.session = requests.Session()
        self.session.headers["authorization"] = get_process_execution_user_token()
    
    def _get_url(self, subpath: str, route: str, template_args: dict=None):
        """Generate an url"""
        subpath_template = string.Template(settings.ROUTES[subpath][route])
        subpath = subpath_template.substitute(**template_args)

        url = f"https://{settings.WAYSCRIPT_HOST}/{subpath}"
        return url

    def get_process_detail_expanded(self, _id: str):
        """Request process expanded detail endpoint"""
        url = self._get_url(subpath="processes", route="detail_expanded", template_args={"id": _id})
        response = self.session.get(url)
        return response

    def get_lair_detail(self, _id: str):
        """Request lair detail"""
        url = self._get_url(subpath="lairs", route="detail", template_args={"id": _id})
        response = self.session.get(url)
        return response

    def get_workspace_detail(self, _id: str):
        """Request workspace detail"""
        url = self._get_url(subpath="workspaces", route="detail", template_args={"id": _id})
        response = self.session.get(url)
        return response
