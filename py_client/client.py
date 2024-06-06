import requests

endpoint = "http://localhost:8000/todo/list/"

message = requests.get(endpoint)

print(message.json(), message.status_code)
