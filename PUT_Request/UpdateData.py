from cgitb import reset

import requests
import json

url = "https://reqres.in/api/users/2"

# Reading the reponse bosy from a file
file_path = open("update_body.json")
json_input = file_path.read()

json_input = json.loads(json_input)

# To perform PUT request
respose = requests.put(url,json_input)
print(respose.content)

# Validating response code
assert respose.status_code == 200