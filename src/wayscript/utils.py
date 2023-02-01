import functools
import os
import string

import requests

from . import settings


def get_process_execution_user_token():
    """Return the auth token of the user this process is executing on behalf of"""
    token = os.environ.get("WAYSCRIPT_EXECUTION_USER_TOKEN")
    return token


def set_process_execution_user_token(value: str):
    os.environ["WAYSCRIPT_EXECUTION_USER_TOKEN"] = value
    return value


def get_process_id():
    """Return uuid of current container execution"""
    process_id = os.environ["WS_PROCESS_ID"]
    return process_id


def get_refresh_token():
    refresh_token = os.environ["WAYSCRIPT_EXECUTION_USER_REFRESH_TOKEN"]
    return refresh_token


def get_application_key():
    application_key = os.environ["WAYSCRIPT_EXECUTION_USER_APPLICATION_KEY"]
    return application_key


def get_lair_url():
    lair_url = os.environ["WAYSCRIPT_LAIR_URL"]
    return lair_url


def retry_on_401_wrapper(f):

    @functools.wraps(f)
    def _retry_on_401(client, *args, **kwargs):

        response = f(client, *args, **kwargs)
        # refresh credentials and retry on 401
        if response.status_code == 401:
            client._refresh_access_token()
            response = f(client, *args, **kwargs)
        return response

    return _retry_on_401


class WayScriptClient:

    def __init__(self, *args, **kwargs):
        """Init a wayscript client"""
        self.session = requests.Session()
        access_token = get_process_execution_user_token()
        self.session.headers["authorization"] = f"Bearer {access_token}"
        self.session.headers["content-type"] = "application/json"

    def _get_url(self, subpath: str, route: str, template_args: dict = None):
        """Generate an url"""
        subpath_template_str = settings.ROUTES[subpath][route]
        subpath_template = string.Template(subpath_template_str)
        full_subpath = subpath_template.substitute(**template_args) if template_args else subpath_template_str

        url = f"{settings.WAYSCRIPT_ORIGIN}/{full_subpath}"
        return url

    def _refresh_access_token(self):
        """Refresh access token and update environment"""
        url = self._get_url(subpath="auth", route="refresh")
        refresh_token = get_refresh_token()
        payload = {"refresh_token": refresh_token}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        set_process_execution_user_token(access_token)
        self.session.headers["authorization"] = f"Bearer {access_token}"

    @retry_on_401_wrapper
    def _send_terminal_output(self, process_id: str, service_id: str, output: str):
        """Send terminal output for current process, for WayScript internal use"""
        payload = {
            'service_id': service_id,
            'process_id': process_id,
            'output': output
        }
        url = self._get_url(subpath="terminal", route="output")
        response = self.session.post(url, json=payload)
        return response

    @retry_on_401_wrapper
    def get_process_detail_expanded(self, _id: str):
        """Request process expanded detail endpoint"""
        url = self._get_url(subpath="processes", route="detail_expanded", template_args={"id": _id})
        response = self.session.get(url)
        return response

    @retry_on_401_wrapper
    def get_workspace_integration_detail(self, _id: str):
        """Request a workspace-integrations detail"""
        url = self._get_url(subpath="workspace-integrations", route="detail", template_args={"id": _id})
        response = self.session.get(url)
        return response

    @retry_on_401_wrapper
    def get_lair_detail(self, _id: str):
        """Request lair detail"""
        url = self._get_url(subpath="lairs", route="detail", template_args={"id": _id})
        response = self.session.get(url)
        return response

    @retry_on_401_wrapper
    def get_workspace_detail(self, _id: str):
        """Request workspace detail"""
        url = self._get_url(subpath="workspaces", route="detail", template_args={"id": _id})
        response = self.session.get(url)
        return response

    @retry_on_401_wrapper
    def post_webhook_http_trigger_response(self, _id: str, payload: dict = None):
        """
        Post an http trigger response

        _id: process id launched by http trigger
        payload: a payload describing how to respond to the http trigger's request
        """
        url = self._get_url(subpath="webhooks", route="http_trigger_response", template_args={"id": _id})
        response = self.session.post(url, json=payload)
        return response

    def get_user_detail_by_application_key(self, application_key: str, workspace_id: str):
        """
        Request user detail using its application key
        """
        url = self._get_url(subpath="workspaces", route="user_application_key_detail", template_args={"id": workspace_id})
        response = self.session.get(url, headers={"authorization": f"Bearer {application_key}"})
        return response

    def set_lair_secret(self, _id: str, secret_key: str, secret_val: str):
        """
        Create a new secret or update an existing secret

        _id: lair id
        secret_key: key to update secret for
        secret_val: value to set secret to (will be encrypted)
        """
        payload = {"key": secret_key, "value": secret_val}
        url = self._get_url(subpath="files", route="set_secret", template_args={"id": _id})
        response = self.session.post(url, json=payload)
        return response
