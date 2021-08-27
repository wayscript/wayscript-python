from wayscript import utils


def send_response(data: dict=None, headers: dict=None, status_code: int=None):
    """Send response to http trigger endpoint"""
    assert data, "data kwarg is required"
    assert headers, "headers kwarg is required"
    assert status_code, "status_code kwarg is required"
    wayscript_client = utils.WayScriptClient()
    response = wayscript_client.get_workspace_integration_detail(_id)
    response.raise_for_status()
    workspace_integration_data = response.json()
