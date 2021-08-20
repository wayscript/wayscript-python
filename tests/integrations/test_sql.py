import pytest
import responses

from wayscript.integrations import sql


PSYCOPG2_EXPECTED = dict(
    dbname="my_db",
    user="zach",
    password="very-secret-password",
    host="host.docker.internal",
    port=15432,
)

MSSQL_EXPECTED = {
    "database": "my_db",
    "password": "very-secret-password",
    "port": 15432,
    "server": "host.docker.internal",
    "user": "zach",
}

MYSQL_EXPECTED = {
    "database": "my_db",
    "host": "host.docker.internal",
    "password": "very-secret-password",
    "port": 15432,
    "user": "zach",
}


@responses.activate
@pytest.mark.parametrize(
    "client_name,expected",
    [
        ("psycopg2", PSYCOPG2_EXPECTED),
        ("mssql", MSSQL_EXPECTED),
        ("mysql", MYSQL_EXPECTED),
    ],
)
def test_get_connection_kwargs(
    client_name,
    expected,
    patch_client_get_url,
    workspace_integrations_detail_response_sql,
):
    """Test getting postgres client kwargs"""

    responses.add(
        responses.GET,
        patch_client_get_url,
        json=workspace_integrations_detail_response_sql,
        status=200,
    )

    _id = workspace_integrations_detail_response_sql["id"]

    function_name = f"get_{client_name}_connection_kwargs"
    function = getattr(sql, function_name)

    assert expected == function(_id)
