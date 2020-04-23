import requests
import json

#API
url = "https://reqres.in/api/users?page=2"

#send get request

response = requests.get(url)

print(response)

#display response content
print(response.content)
#print(response.headers)
#print(json.dumps(response.json(), indent=4))
print(response.status_code)

#validate status code
assert response.status_code == 200

#fetch response headers
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#fetch cookies
print(response.cookies)

#fetch encoding
print(response.encoding)

#fetch elapsed time
print(response.elapsed)