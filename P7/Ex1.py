import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
print(response.status)
answer_decoded = response.read().decode()
print(type(answer_decoded), answer_decoded)
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)
if dict_response['ping'] == 1:
    print('PING OK! DATA BASE IS RUNNING')
else:
    print('DATA BASE IS DOWN')