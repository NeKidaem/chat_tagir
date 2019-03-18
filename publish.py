import json
import requests

api_key = '634d57c8-ae82-42b7-b84d-266b724d2f19'
command = {
    "method": "publish",
    "params": {
        "channel": "docs", 
        "data": {
            "content": "1"
        }
    }
}

api_key = api_key
data = json.dumps(command)
headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + api_key}
resp = requests.post("http://localhost:8000/api", data=data, headers=headers)
print(resp.json())
