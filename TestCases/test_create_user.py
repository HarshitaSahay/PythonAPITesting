import requests
import json
import allure

def test_create_new_user(self):
    # API Url

    url = "https://reqres.in/api/users"

    # Read input json file

    file = open('C:/Users/Harshita Sahay/PycharmProjects/RestAPIAutomation/CreateUser.json', 'r')
    json_input = file.read()

    # Parse file input to json format
    request_json = json.loads(json_input)

    print(request_json)

    # Make a POST request with json input body
    response = requests.post(url, request_json)

    # print(response.content)
    print(json.loads(response.text))
    print(json.dumps(response.json(), indent=4))
    assert response.status_code == 201

#test_create_new_user()