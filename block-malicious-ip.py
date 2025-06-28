# Sample Python script to block a malicious IP
import requests

FIREWALL_API_URL = "https://api.firewall.com/block"
API_KEY = "your_api_key_here"

def block_ip(ip_address):
    payload = {"ip": ip_address, "action": "block"}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(FIREWALL_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Blocked IP {ip_address} successfully.")
    else:
        print(f"Failed to block IP {ip_address}. Status: {response.status_code}")

if __name__ == "__main__":
    ip = input("Enter IP to block: ")
    block_ip(ip)
