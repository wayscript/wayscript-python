import pytest
import responses

from wayscript import settings, utils

@responses.activate
@pytest.mark.parametrize(
    "method,_id,expected_subpath",
    [
        ("get_workspace_detail", "19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0", "workspaces/19cb0a0f-f48c-4191-84b5-ba7be8ceb1a0"),
        ("get_lair_detail","334d88dc-f9bf-4d3e-a7a2-0dec1279e4d9", "lairs/334d88dc-f9bf-4d3e-a7a2-0dec1279e4d9"),
        ("get_process_detail_expanded","378daaa4-0fc3-48da-9f51-f745151dfc08", "processes/378daaa4-0fc3-48da-9f51-f745151dfc08/detail"),
        ("get_workspace_integration_detail","9b3e827e-f113-41fc-a14e-4ba53afa1707", "workspace-integrations/9b3e827e-f113-41fc-a14e-4ba53afa1707"),
    ],
)
def test__get_url_generates_correct_endpoints(method, _id, expected_subpath):
    """Test that wayscript client's _get_url method generates the correct expected url subpath"""
    
    expected_url = f"{settings.WAYSCRIPT_ORIGIN}/{expected_subpath}"
    responses.add(responses.GET, expected_url,
                  json={}, status=200)

    client = utils.WayScriptClient()
    callable = getattr(client, method)
    callable(_id)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url


