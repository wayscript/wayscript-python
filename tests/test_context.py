from wayscript import context as ws_context

def test_hello_world():
    assert "hello, world" == ws_context.hello_world()
