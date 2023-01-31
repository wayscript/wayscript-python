import json
import os

import pytest


@pytest.fixture(autouse=True)
def stub_environment():
    stubbed_environment_variables = [
        "WAYSCRIPT_EXECUTION_USER_TOKEN",
        "WS_PROCESS_ID",
        "WAYSCRIPT_EXECUTION_USER_REFRESH_TOKEN",
        "WAYSCRIPT_EXECUTION_USER_APPLICATION_KEY",
        "WAYSCRIPT_LAIR_URL",
    ]

    for var in stubbed_environment_variables:
        os.environ[var] = "TEST_SETTING"


LAIR_ID = "61429be0-25a0-4030-a824-0e34163e441e"
WORKSPACE_ID = "fbcb455f-0d49-4fb7-b6d4-44e005a3ca42"
WORKSPACE_INTEGRATION_ID = "9b3e827e-f113-41fc-a14e-4ba53afa1707"


@pytest.fixture
def patch_client_get_url(monkeypatch):
    from wayscript.utils import WayScriptClient

    patched_url = "https://test-test-test.wayscript.com/a-new-route"
    monkeypatch.setattr(WayScriptClient, "_get_url", lambda *args, **kwargs: patched_url)
    return patched_url


@pytest.fixture
def processes_detail_expanded_response():
    """Data representing a response from the `processes-detail-expanded` endpoint"""
    data = {
        "event": {
            "created_date": "2021-07-22T14:57:06.461182",
            "data": {"hello": "world"},
            "id": "d1e498e4-2f32-4e5c-803e-d5fe1e2b89fe",
            "trigger_type": "cron"},
        "lair_trigger": {
            "created_date": "2021-07-22T14:57:06.456127",
            "data": None,
            "entrypoint": None,
            "lair_id": LAIR_ID,
            "settings": None,
            "test_event": "sample-test-event",
            "trigger_id": "081f3cfe-b9ba-4e6c-9f9a-d20206d3a3ee",
            "type": "cron"},
        "process": {
            "command": None,
            "created_date": "2021-07-22T14:57:06.466253",
            "event_id": "d1e498e4-2f32-4e5c-803e-d5fe1e2b89fe",
            "id": "dd57b3d9-52aa-4407-84ca-3ef998757aa1",
            "lair_id": LAIR_ID,
            "port": None,
            "service_id": "42621a34-cbab-48f3-a3d2-400d83868caf",
            "status": None,
            "trigger_id": "081f3cfe-b9ba-4e6c-9f9a-d20206d3a3ee"
        }
    }
    return data


@pytest.fixture
def lairs_detail_response():
    """Data representing a response from `GET /lairs/<id>`"""
    data = {
        "created_date": "Thu, 22 Jul 2021 15:40:23 GMT",
        "file_object": "",
        "internal_id": "122",
        "lair_manager": "0faa1b77-0e54-4d50-83d4-412a972bc99b",
        "lair_name": "a6ed446a-2cb6-4421-98f5-3352020f2db8",
        "id": LAIR_ID,
        "last_run_date": "Thu, 22 Jul 2021 15:40:23 GMT",
        "workspace_id": WORKSPACE_ID,
    }

    return data


@pytest.fixture
def user_detail_response():
    """Data representing a response from GET /workspaces/<id>/users/self"""
    data = {
        "avatar": "https://lh3.googleusercontent.com/a-/BOh14LjZkR7iuACWXfkCrZX3nixJCdRUc_3PYP9wu7CA=s96-c",
        "created_date": "2021-12-15T03:18:23.865839",
        "email": "foobar@fooey.com",
        "first_name": "John",
        "id": "705c088f-1211-4c0e-a520-1d5f76b6940e",
        "last_name": "Jingleheimerschmidt"
    }
    return data


@pytest.fixture
def workspaces_detail_response():
    """Data from GET /workspaces/<id>"""
    data = {
        "file_object": "",
        "workspace_name": "fbb01af8-c476-4928-8921-b12e9ba91436",
        "workspace_id": WORKSPACE_ID,
    }
    return data


@pytest.fixture
def workspace_integrations_detail_response():
    """Data from GET /workspaces-integrations/<id>"""
    data = {
        "id": WORKSPACE_INTEGRATION_ID,
        "type": "slack",
        "credentials": json.dumps({
            "access_token": "d259c1df-0ef0-4f62-8458-3548bbf5c28d"
        })
    }
    return data


@pytest.fixture
def workspace_integration_sql_credentials():
    """Data for sql credentials"""
    data = {
        "database_name": "my_db",
        "database_user": "zach",
        "database_port": 15432,
        "database_password": "very-secret-password",
        "database_host": "host.docker.internal"
    }
    return data


@pytest.fixture
def workspace_integrations_detail_response_sql(workspace_integration_sql_credentials):
    """
    Data from GET /workspaces-integrations/<id>

    For type=sql
    """
    data = {
        "id": WORKSPACE_INTEGRATION_ID,
        "type": "sql",
        "credentials": json.dumps(workspace_integration_sql_credentials),
    }
    return data
