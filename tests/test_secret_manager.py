import responses

from wayscript import secret_manager
from wayscript.errors import UnauthorizedUserError


@responses.activate
def test_set_secret(patch_client_get_url):
    """Test set secret"""
    responses.add(responses.POST, patch_client_get_url, json={}, status=200)

    secret_manager.set_secret("test_key", "test_val")


@responses.activate
def test_set_secret_unauthorized_user(patch_client_get_url):
    """Test that set secret raises the appropriate error for unauthorized users"""
    responses.add(responses.POST, patch_client_get_url, json={}, status=403)

    try:
        secret_manager.set_secret("test_key", "test_val")
    except UnauthorizedUserError:
        assert True
