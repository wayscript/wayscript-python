import json

import psycopg2

from wayscript import utils
from wayscript.errors import MissingCredentialsError


def get_connection_kwargs(_id: str) -> dict:
    """
    Return postgres connection kwargs
    
    If you want to instantiate your own client, use this method.
    """
    wayscript_client = utils.WayScriptClient()
    response = wayscript_client.get_workspace_integration_detail(_id)
    response.raise_for_status()
    workspace_integration_data = response.json()
    credentials_str = workspace_integration_data.get("credentials")
    credentials = {}

    try:
        credentials = json.loads(credentials_str)
    except json.decoder.JSONDecodeError:
        credentials = {}

    kwargs = {
        "dbname": credentials.get("database_name"),
        "user": credentials.get("database_user"),
        "password": credentials.get("database_password"),
        "host": credentials.get("database_host"),
        "port": credentials.get("database_port", 5432),
    }

    if not credentials or not all(v for v in kwargs.values()):
        raise MissingCredentialsError(f"Missing credentials for workspace_integration={_id}")

    return kwargs


def get_client_for_workspace_integration(_id: str):
    """Instantiate connection from workspace integration kwargs"""
    kwargs = get_connection_kwargs(_id)
    return psycopg2.connect(**kwargs)
