from wayscript.integrations.sql import postgres

_id = "c227ed10-1174-4722-a25a-1e5d3f770ad2"
conn = postgres.get_client_for_workspace_integration(_id)

with conn.cursor() as cursor:
    cursor.execute("SELECT *  FROM public.event;")
    print(len([x for x in cursor]))
