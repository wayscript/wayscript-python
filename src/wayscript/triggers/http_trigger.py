from wayscript import utils


def send_response(data: dict=None, headers: dict=None, status_code: int=None):
    """Send response to http trigger endpoint"""
    assert data, "data kwarg is required"
    assert headers, "headers kwarg is required"
    assert status_code, "status_code kwarg is required"
    wayscript_client = utils.WayScriptClient()
    process_id = utils.get_process_id()
    payload = {
        "data": data,
        "headers": headers,
        "status_code": status_code,
    }
    response = wayscript_client.post_webhook_http_trigger_response(process_id, payload)
    response.raise_for_status()

    return response
