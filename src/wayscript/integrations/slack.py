import json

from slack_sdk import WebClient

from wayscript import utils
from wayscript.errors import MissingCredentialsError


def get_client_for_workspace_integration(_id: str) -> WebClient:
    """Get a slack client with credentials from a workspace integration"""
    wayscript_client = utils.WayScriptClient()
    response = wayscript_client.get_workspace_integration_detail(_id)
    response.raise_for_status()
    workspace_integration_data = response.json()

    access_token = None
    credentials_str = workspace_integration_data["credentials"]

    try:
        credentials = json.loads(credentials_str)
        access_token = credentials.get("access_token")
    except json.decoder.JSONDecodeError:
        access_token = None
    
    if not access_token:
        raise MissingCredentialsError(f"No credentials found for {_id}")
    else:
        return WebClient(access_token)
