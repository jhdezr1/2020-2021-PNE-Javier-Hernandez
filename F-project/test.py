import http.client
import json
SERVER = "rest.ensembl.org"
ENDPOINT1 = '/info/species'
ENDPOINT2 = '/info/assembly'
# between endpoint2 and parameters2 add the species (but not the display name that i did in the first exercise)
PARAMETERS2 = '?bands=1&content-type=application/json'
PARAMETERS1 = '?content-type=application/json'
# Create connection with ensembl database
connection = http.client.HTTPConnection(SERVER)
# connect with the first endpoint
connection.request('GET', ENDPOINT1 + PARAMETERS1)
response = connection.getresponse()
# getting the dictionary
response_dict = json.loads(response.read().decode())
# putting all of the species into one list
species_full = response_dict['species']
species_name = []
for e in species_full:
    species_name.append(e['display_name'])

print(species_full)