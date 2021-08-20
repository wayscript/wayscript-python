import json

from wayscript import utils
from wayscript.errors import MissingCredentialsError


PSYCOPG2_CONNECTION_KWARG_MAP = {
        "dbname": "database_name",
        "user": "database_user",
        "password": "database_password",
        "host": "database_host",
        "port": "database_port",
}


MSSQL_CONNECTION_KWARG_MAP = {
    "server": "database_host",
    "user": "database_user",
    "password": "database_password",
    "database": "database_name",
    "port": "database_port",

}


MYSQL_CONNECTION_KWARG_MAP = {
    "host": "database_host",
    "user": "database_user",
    "password": "database_password",
    "database": "database_name",
    "port": "database_port",
}


def get_connection_kwargs(_id: str, credentials_mapping: dict) -> dict:
    """
    Return connection kwargs
    
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

    kwargs = {k: credentials.get(v) for k, v in credentials_mapping.items()}

    if not credentials:
        raise MissingCredentialsError(f"Missing credentials for workspace_integration={_id}")

    return kwargs

def get_psycopg2_connection_kwargs(_id: str) -> dict:
    """Get connection kwargs for psycopg2"""
    return get_connection_kwargs(_id, credentials_mapping=PSYCOPG2_CONNECTION_KWARG_MAP)

def get_mssql_connection_kwargs(_id: str) -> dict:
    """Get connection kwargs for SQL Server connection via mssql driver"""
    return get_connection_kwargs(_id, credentials_mapping=MSSQL_CONNECTION_KWARG_MAP)

def get_mysql_connection_kwargs(_id: str) -> dict:
    """Return connection kwargs for MySQL connection via mysql driver"""
    return get_connection_kwargs(_id, credentials_mapping=MYSQL_CONNECTION_KWARG_MAP)
