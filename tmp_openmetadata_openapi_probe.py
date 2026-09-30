from dotenv import dotenv_values
import httpx

env = dotenv_values('.env')
url = 'http://localhost:8585'
token = env.get('OPENMETADATA_TOKEN')
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

with httpx.Client(base_url=url, headers=headers, timeout=10) as client:
    for path in ['/api/v1/openapi', '/api/v1/docs', '/api/v1/swagger', '/openapi.json', '/swagger.json']:
        try:
            r = client.get(path)
            print(path, r.status_code, r.headers.get('content-type'))
            if r.status_code == 200:
                print(r.text[:1000])
                break
        except Exception as e:
            print(path, 'err', e)
