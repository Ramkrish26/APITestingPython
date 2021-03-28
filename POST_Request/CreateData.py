import requests
import json

url = "https://reqres.in/api/users"

# Reading the reponse bosy from a file
file_path = open("create_body.json")
json_input = file_path.read()

json_input = json.loads(json_input)

# To perform post requst
response = requests.post(url,json_input)
print(response.content)

# Asserting the response code of POST method
assert response.status_code == 201