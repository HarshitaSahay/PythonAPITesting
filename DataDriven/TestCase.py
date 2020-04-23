import requests
import openpyxl
import json
import jsonpath
from DataDriven import Library

def test_add_multiple_students():
    #API
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\Harshita Sahay\\PycharmProjects\\RestAPIAutomation\\AddNewStudent.json')
    json_request = json.loads(f.read())

    obj = Library.Common('C:\\Users\\Harshita Sahay\\PycharmProjects\\RestAPIAutomation\\TestMultipleData.xlsx', 'Sheet1')
    cols = obj.fetch_column_count()
    rows = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, rows+1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        requests.post(api_url, updated_json_request)
        response = requests.post(api_url, json_request)

        #print(response.text)
        print(response.status_code)
        assert response.status_code == 201
