# Sample Python script to disable a compromised user
import requests

API_URL = "https://api.identity.com/disable-user"
API_KEY = "your_api_key_here"

def disable_user(username):
    payload = {"username": username, "action": "disable"}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Disabled user {username} successfully.")
    else:
        print(f"Failed to disable user {username}. Status: {response.status_code}")

if __name__ == "__main__":
    user = input("Enter username to disable: ")
    disable_user(user)
