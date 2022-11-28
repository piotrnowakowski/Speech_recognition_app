import requests
import json
"""
r = requests.get('http://127.0.0.1:8080/example')
print(r.headers)
print(r.status_code)

pload = 'work'
r = requests.post('http://127.0.0.1:8080/example',data = pload)
print(r.text)
"""

text = "hi"

url = "http://localhost:5005/webhooks/rest/webhook"
obj_to_send = {
    "sender": "test_user",
    "message": text
}
req = requests.post(url, json.dumps(obj_to_send))
if req.status_code == requests.codes.ok:
    print("it's okey")
    print(req.text)
else:
    print("somethin is wrong")