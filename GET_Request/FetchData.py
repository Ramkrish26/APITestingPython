from contextlib import redirect_stderr

import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
# print(response)

# Display Response content
# print(response.content)

# To parse the reposne into a json response
json_response = json.loads(response.text)
print(json_response)

# To fetch value using json path
print(jsonpath.jsonpath(json_response,'total'))

# To display headers of a response
# print(response.headers)

# Validate response code
# assert response.status_code == 200

# To fetch specific value from a key in header
# print(response.headers.get("date"))

# To fetch time durartion of request and response
# print(response.elapsed)