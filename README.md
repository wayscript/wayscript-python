# wayscript-python

## Triggers

### HTTP Triggers

```
from wayscript.triggers import http_trigger

payload = {"hello": "world"}
headers = {"content-type": "application/json"}
status_code = 200

http_trigger.send_response(data=payload, headers=headers, status_code=status_code)
```

## Integrations

### SQL

To connect to a postgres resource, use the following snippet:
```
import psycopg2
from wayscript.ingegrations import sql

kwargs = sql.get_psycopg2_connection_kwargs(_id)
connection = psycopg2.connect(**kwargs)
```
