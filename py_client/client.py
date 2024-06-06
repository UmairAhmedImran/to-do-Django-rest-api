import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/todo/auth/"

username = input("What is your username: ")
password = getpass("what is password: ")
auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password})

print(auth_response.json(), auth_response.status_code)

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    header = {
        "Authorization": f"Token {token}"
    }
    endpoint = "http://localhost:8000/todo/"

    message = requests.get(endpoint, headers=header)

    print(message.json(), message.status_code)
