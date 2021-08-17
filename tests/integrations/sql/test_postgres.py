from unittest import mock

import psycopg2
import responses

from wayscript.integrations.sql import postgres


@responses.activate
def test_get_postgres_client_for_workspace_integration(
    monkeypatch,
    patch_client_get_url,
    workspace_integration_sql_credentials,
    workspace_integrations_detail_response_sql,
):
    """Test getting postgres client kwargs"""
    connection = "my-connection"
    monkeypatch.setattr(psycopg2, "connect", mock.Mock(return_value=connection))

    responses.add(
        responses.GET,
        patch_client_get_url,
        json=workspace_integrations_detail_response_sql,
        status=200,
    )

    _id = workspace_integrations_detail_response_sql["id"]

    assert connection == postgres.get_client_for_workspace_integration(_id)

    psycopg2.connect.assert_called_with(dbname='my_db', user='zach', password='very-secret-password', host='host.docker.internal', port=15432)