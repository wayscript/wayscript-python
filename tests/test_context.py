import pytest
import responses
import requests

from wayscript import context as ws_context
from wayscript import settings as ws_settings


@responses.activate
@pytest.mark.parametrize(
    "response_key",
    [("process"), ("event"), ("lair_trigger")],
)
def test_process_expanded_detail_methods(patch_client_get_url, processes_detail_expanded_response, response_key):
    """Test functions that return data from the processes expanded detail call"""
    responses.add(responses.GET, patch_client_get_url,
                  json=processes_detail_expanded_response, status=200)

    callable = getattr(ws_context, f"get_{response_key}")
    assert callable() == processes_detail_expanded_response[response_key]

@responses.activate
def test_get_lair(patch_client_get_url, lairs_detail_response):
    """Test returning lair data"""
    responses.add(responses.GET, patch_client_get_url,
                  json=lairs_detail_response, status=200)

    assert ws_context.get_lair() == lairs_detail_response


@responses.activate
def test_get_workspace(patch_client_get_url, lairs_detail_response, workspaces_detail_response, monkeypatch):
    """Test returning workspace data"""
    responses.add(responses.GET, patch_client_get_url,
                  json=workspaces_detail_response, status=200)
    
    monkeypatch.setattr(ws_context, "get_lair", lambda *args, **kwargs: lairs_detail_response)

    workspace = ws_context.get_workspace()
    assert workspace == workspaces_detail_response
