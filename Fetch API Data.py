import requests

response = requests.get("https://api.github.com/users/Smugu290")
print(response.json())
