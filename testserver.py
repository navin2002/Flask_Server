import requests

res=requests.get("http://localhost:5000/backend")
print(res.json())