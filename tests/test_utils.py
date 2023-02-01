import pytest
import responses
import json
from uuid import uuid4

from wayscript import settings, utils
from unittest import mock


@responses.activate
@pytest.mark.parametrize(
    "method,_id,expected_subpath,http_method",
    [
        ("get_lair_detail", "334d88dc-f9bf-4d3e-a7a2-0dec1279e4d9", "lairs/334d88dc-f9bf-4d3e-a7a2-0dec1279e4d9", "GET"),
        ("get_process_detail_expanded", "378daaa4-0fc3-48da-9f51-f745151dfc08", "processes/378daaa4-0fc3-48da-9f51-f745151dfc08/detail", "GET"),
        ("post_webhook_http_trigger_response", "19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0", "webhooks/http-trigger/response/19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0", "POST"),
        ("get_workspace_detail", "19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0", "workspaces/19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0", "GET"),
        ("get_workspace_integration_detail", "9b3e827e-f113-41fc-a14e-4ba53afa1707", "workspace-integrations/9b3e827e-f113-41fc-a14e-4ba53afa1707", "GET"),
    ],
)
def test__get_url_generates_correct_endpoints(method, _id, expected_subpath, http_method):
    """Test that wayscript client's _get_url method generates the correct expected url subpath"""

    expected_url = f"{settings.WAYSCRIPT_ORIGIN}/{expected_subpath}"
    responses_method = getattr(responses, http_method)
    responses.add(responses_method, expected_url,
                  json={}, status=200)

    client = utils.WayScriptClient()
    callable = getattr(client, method)
    callable(_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url


@responses.activate
def test__send_terminal_output():
    """Test that _send_terminal_output sends the correct payload to the proper url"""
    process_id = str(uuid4())
    service_id = str(uuid4())
    output = "Hello World"

    expected_payload = {
        "process_id": process_id,
        "service_id": service_id,
        "output": output,
    }
    expected_url = f"{settings.WAYSCRIPT_ORIGIN}/terminal/output"
    responses.add("POST", expected_url,
                  json={}, status=200)

    client = utils.WayScriptClient()
    client._send_terminal_output(process_id, service_id, output)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert json.loads(responses.calls[0].request.body) == expected_payload


@pytest.mark.parametrize(
    "method,env_var_name",
    [
        ("get_process_execution_user_token","WAYSCRIPT_EXECUTION_USER_TOKEN"),
        ("get_process_id","WS_PROCESS_ID"),
        ("get_application_key","WAYSCRIPT_EXECUTION_USER_APPLICATION_KEY"),
        ("get_refresh_token","WAYSCRIPT_EXECUTION_USER_REFRESH_TOKEN"),
        ("get_lair_url","WAYSCRIPT_LAIR_URL"),
    ]
)
def test__get_env_var(method, env_var_name):
    """Test that getting environment variables functions as expected"""
    expected = str(uuid4())
    with mock.patch.dict('os.environ', { env_var_name: expected }, clear=True):
        callable = getattr(utils, method)
        resp = callable()

        assert resp == expected
