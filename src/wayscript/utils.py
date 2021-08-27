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
        access_token =  get_process_execution_user_token()
        self.session.headers["authorization"] = f"Bearer {access_token}"
        self.session.headers["content-type"] = "application/json"
    
    def _get_url(self, subpath: str, route: str, template_args: dict=None):
        """Generate an url"""
        subpath_template = string.Template(settings.ROUTES[subpath][route])
        subpath = subpath_template.substitute(**template_args)

        url = f"{settings.WAYSCRIPT_ORIGIN}/{subpath}"
        return url

    def get_process_detail_expanded(self, _id: str):
        """Request process expanded detail endpoint"""
        url = self._get_url(subpath="processes", route="detail_expanded", template_args={"id": _id})
        response = self.session.get(url)
        return response

    def get_workspace_integration_detail(self, _id: str):
        """Request a workspace-integrations detail"""
        url = self._get_url(subpath="workspace-integrations", route="detail", template_args={"id": _id})
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

    def post_webhook_http_trigger_response(self, _id: str):
        """
        Post an http trigger response
        
        _id: process id launched by http trigger
        """
        url = self._get_url(subpath="webhooks", route="http_trigger_response", template_args={"id": _id})
        response = self.session.post(url)
        return response
