from urllib.error import HTTPError

from . import utils, context, errors

def set_secret(secret_key: str, secret_val: str) -> None:
    process_details = context.get_process()
    lair_id = process_details["lair_id"]
    client = utils.WayScriptClient()
    response = client.set_lair_secret(lair_id, secret_key, secret_val)
    
    # Handle unhelpful error cases
    try:
        response.raise_for_status()
    except HTTPError as e:
        if e.code == 403:
            raise errors.UnauthorizedUserError
        else:
            raise e
