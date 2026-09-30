from dotenv import dotenv_values
import httpx

env = dotenv_values('.env')
url = 'http://localhost:8585'
token = env.get('OPENMETADATA_TOKEN')
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

with httpx.Client(base_url=url, headers=headers, timeout=10) as client:
    version = client.get('/api/v1/system/version')
    print('version status', version.status_code)
    print('version body', version.text)
    dbschema = client.get('/api/v1/databaseSchemas', params={'limit': 1})
    print('dbschema status', dbschema.status_code)
    print('dbschema body', dbschema.text)
