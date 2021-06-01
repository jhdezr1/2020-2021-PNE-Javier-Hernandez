import http.client
import server_utils as su

PORT = 8081
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)
JSON_PARAM = '&json=1'


# BASIC LEVEL ENDPOINTS

# -- '/' ENDPOINT
ENDPOINT = '/'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT + '?')}" + '\n')

# -- '/listSpecies' ENDPOINT

ENDPOINT = '/listSpecies?limit=2'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')


ENDPOINT = '/listSpecies?limit='
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')

# -- '/karyotype' ENDPOINT
ENDPOINT = '/karyotype?specie=human'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')

# -- '/chromosomeLength' ENDPOINT
ENDPOINT = '/chromosomeLength?specie=human&chromo=X'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')

# MEDIUM LEVEL ENDPOINTS

# -- '/geneSeq' ENDPOINT
ENDPOINT = '/geneSeq?gene=RNU6_269P'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')

# -- '/geneInfo' ENDPOINT
ENDPOINT = '/geneInfo?gene=RNU6_269P'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')

# -- '/geneCalc' ENDPOINT
ENDPOINT = '/geneCalc?gene=RNU6_269P'
print(f"----------------testing {ENDPOINT}-----------------")

print(f"CONTENT: {su.test_endpoint_json(ENDPOINT)}" + '\n')
