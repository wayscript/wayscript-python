import pytest
import responses

from wayscript import secret_manager as ws_secret_manager


@responses.activate
def test_set_secret(patch_client_get_url):
    """Test set secret"""
    responses.add(responses.POST, patch_client_get_url, json={}, status=200)

    callable = getattr(ws_secret_manager, 'set_secret')
    assert callable("test_key", "test_val") == True
