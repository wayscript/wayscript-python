import os

import integration_service


def hello_world():
    """No-op to test linting/testing CI"""
    return "hello, world"

def get_process():
    """
    Return metadata about the current execution process
    
    This could include things like start time, calculated run time, state, the "execution user", etc.
    """
    process_uuid = os.environ["WS_SCRIPT_PROCESS_UUID"]
    process_data = integration_service.get_process(process_uuid)
    return process_data


# are half of these just pass through calls to the integration service? what value does wayscript.context provide as a wrapper? where do we draw the line?
def get_event():
    """Returns the event object of the execution context"""
    pass


def get_trigger():
    """Returns information about the trigger that launched the event"""
    pass


def get_lair():
    """Returns lair metadata"""
    pass


def get_workspace():
    """Return workspace metadata"""
    pass


def get_execution_user():
    """Do we want to create a notion of a "user that this script is being executed as"? Or should we just allow people to look up the lair owner?
    
    I think we need to establish a notion of an execution user because we need to be able to communicate to developers
    who api calls will be made on behalf of against wayscript endpoints.

    For now, this can just proxy the lair owner. But I think having this layer of abstraction (might?) help us in future when we have more sophisticated execution models?
    """