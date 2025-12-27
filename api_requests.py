import requests
import json

print(requests.get("https://jsonplaceholder.typicode.com/todos/1").text)

response=requests.get("https://api.github.com/users/Mosultan1068")
print(response)
data=response.json()
print(json.dumps(data, indent=4))

url="https://api.github.com/users/Mosultan1068"
token="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"
data = {"name" "new_repos-1"}
response = requests.post(url, json=data, headers={"Authorization": f"token {token}"})

print(response.json())