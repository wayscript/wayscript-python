import os
from functools import lru_cache

from . import utils


@lru_cache()
def _get_process_detail_expanded_data() -> dict:
    """Wrapper to cache data from process_detail_expanded call"""
    process_uuid = utils.get_process_uuid()
    client = utils.WayScriptClient()
    response = client.get_process_detail_expanded(process_uuid)
    response.raise_for_status()
    return response.json()


def get_process():
    """
    Return metadata about the current execution process.
    """
    data = _get_process_detail_expanded_data()["process"]
    return data


# are half of these just pass through calls to the integration service? what value does wayscript.context provide as a wrapper? where do we draw the line?
def get_event():
    """Returns the event object of the execution context"""
    data = _get_process_detail_expanded_data()["event"]
    return data


def get_lair_trigger():
    """Returns information about the trigger that launched the event"""
    data = _get_process_detail_expanded_data()["lair_trigger"]
    return data


def get_lair():
    """Returns lair metadata"""
    lair_trigger = get_lair_trigger()
    lair_id = lair_trigger["lair_id"]
    client = utils.WayScriptClient()
    response = client.get_lair_detail(lair_id)
    response.raise_for_status()
    data = response.json()
    return data


def get_workspace():
    """Return workspace metadata"""
    lair_data = get_lair()
    workspace_id = lair_data["workspace_uuid"]
    client = utils.WayScriptClient()
    response = client.get_workspace_detail(workspace_id)
    response.raise_for_status()
    data = response.json()
    return data
