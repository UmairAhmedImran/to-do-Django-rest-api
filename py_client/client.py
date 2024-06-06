import requests

endpoint = "http://localhost:8000/todo/"

message = requests.get(endpoint)

print(message.json(), message.status_code)
