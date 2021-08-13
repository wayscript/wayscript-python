import uuid

import pytest
import responses

from slack_sdk import WebClient

from wayscript.integrations import slack

@responses.activate
def test_slack_get_client_for_workspace_integration(workspace_integrations_detail_response, patch_client_get_url):
    """Test that we can retrieve a slack client from an integration"""

    responses.add(responses.GET, patch_client_get_url,
                  json=workspace_integrations_detail_response, status=200)
    _id = workspace_integrations_detail_response["id"]
    client = slack.get_client_for_workspace_integration(_id)
    assert isinstance(client, WebClient)

