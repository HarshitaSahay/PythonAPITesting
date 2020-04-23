import requests
headerdata = {'H1':'First_Header', 'H2':'Second_Header'}
response = requests.get('https://httpbin.org/get', headers=headerdata)

print(response.text)