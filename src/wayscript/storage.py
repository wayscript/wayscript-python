from . import context
from .utils import WayScriptClient
from io import BufferedReader, BytesIO

def write_bytes_to_storage(storage_file_path: str, bytes: bytes):
    workspace_info = context.get_workspace()
    name = workspace_info['name']
    client = WayScriptClient()
    file_obj = BufferedReader(BytesIO(bytes))
    res = None
    try:         
        res = client.write_storage_file(name, storage_file_path, file_obj)
    finally:
        file_obj.close()
    return res  

def write_lair_file_to_storage(storage_file_fpath: str, local_file_name: str):
    workspace_info = context.get_workspace()
    name = workspace_info['name']
    client = WayScriptClient()
    with open(local_file_name, 'rb') as file_obj:
        res = client.write_storage_file(name, storage_file_fpath, file_obj)
    return res

def read_storage_file_contents(storage_file_fpath: str):
    workspace_info = context.get_workspace()
    name = workspace_info['name']
    client = WayScriptClient()
    res = client.read_storage_file(name, storage_file_fpath)
    return res