import requests

request = requests.get('http://127.0.0.1:8000/random/100')
print(request.json())