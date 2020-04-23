import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

# Parse response to json format
json_response = json.loads(response.text)
print(json_response)

#pages = jsonpath.jsonpath(json_response,'total_pages')
#print(pages[0])
#assert pages[0] == 2
for i in range(0,6):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))
