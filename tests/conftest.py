import os

import pytest


@pytest.fixture(autouse=True)
def stub_environment():
    
    stubbed_environment_variables = [
        "WAYSCRIPT_EXECUTION_USER_TOKEN",
        "WAYSCRIPT_PROCESS_UUID",
    ]

    for var in stubbed_environment_variables:
        os.environ[var] = "TEST_SETTING"

LAIR_ID = "61429be0-25a0-4030-a824-0e34163e441e"
WORKSPACE_ID = "fbcb455f-0d49-4fb7-b6d4-44e005a3ca42"

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
    """Data representing a response from `GET /lairs/<lair_uuid>`"""
    data = {
        "created_date": "Thu, 22 Jul 2021 15:40:23 GMT",
        "file_object": "",
        "internal_id": "122",
        "lair_manager": "0faa1b77-0e54-4d50-83d4-412a972bc99b",
        "lair_name": "a6ed446a-2cb6-4421-98f5-3352020f2db8",
        "lair_uuid": LAIR_ID,
        "last_run_date": "Thu, 22 Jul 2021 15:40:23 GMT",
        "workspace_uuid": WORKSPACE_ID,
    }

    return data


@pytest.fixture
def workspaces_detail_response():
    """Data from GET /workspaces/<id>"""
    data = {
        "file_object": "",
        "workspace_name": "fbb01af8-c476-4928-8921-b12e9ba91436",
        "workspace_uuid": WORKSPACE_ID,
 }
    return data
