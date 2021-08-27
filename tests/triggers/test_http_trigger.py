from wayscript.triggers import http_trigger

def test_send_response():
    """Test sending response via http trigger"""

    headers = {"content-type": "application"}
    data = {"hello": "world"}
    http_trigger.send_response(data=data, headers=headers, status_code=200)

