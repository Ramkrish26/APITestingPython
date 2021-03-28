import requests
import json

url = "https://reqres.in/api/users/2"

# To do a delete request
response = requests.delete(url)
print(response.status_code)
