# wayscript-python

## Context

```
from wayscript import context

event = context.get_event()
```

### Checking user by application key
```
from wayscript import context, utils

application_key = utils.get_application_key()
user = context.get_user_by_application_key(application_key)
```
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
from wayscript.integrations import sql

kwargs = sql.get_psycopg2_connection_kwargs(_id)
connection = psycopg2.connect(**kwargs)
```

## Secrets

### Create/Update Secret

To create a new secret, or update an existing one:
```
from wayscript import secret_manager

my_secret_value = "an application key or other private information"
secret_manager.set_secret('my_secret_key', my_secret_value)
    
```

To test an existing secret, and update if the secret is no longer valid (expired authorization token):
```
import os
from wayscript import secret_manager

# Retrieve existing key from secret
auth_key = os.getenv('AUTH_KEY_MAY_EXPIRE')

# Test connection to service using auth_key
if not authorized:
    # Get new auth_key from service
    auth_key = 'New Key From Service Request'
    secret_manager.set_secret('AUTH_KEY_MAY_EXPIRE', auth_key)

# Continue flow as normal
```
