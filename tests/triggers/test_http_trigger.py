import responses
from wayscript.triggers import http_trigger


@responses.activate
def test_send_response(patch_client_get_url):
    """Test sending response via http trigger"""
    expected_response = {"message": "ok"}
    responses.add(
        responses.POST, patch_client_get_url, json=expected_response, status=200
    )
    headers = {"content-type": "application"}
    data = {"hello": "world"}
    response = http_trigger.send_response(data=data, headers=headers, status_code=200)

    assert expected_response == response.json()
