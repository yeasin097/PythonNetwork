import requests

response = requests.get("https://managementdu.ac.bd/upload/")

print(response.text)
