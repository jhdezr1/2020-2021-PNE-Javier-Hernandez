import http.client
import json
import Seq1
DICT_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}
LIST_OF_GENES = list(DICT_GENES.keys())
SERVER = "rest.ensembl.org"
ENDPOINT = '/sequence/id/'
PARAMETERS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
for gene in LIST_OF_GENES:
    try:
        id = DICT_GENES[gene]
        connection.request('GET', ENDPOINT + id + PARAMETERS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            sequence = Seq1.Seq(response_dict['seq'])
            s_len = sequence.len()
            info_dict = sequence.info_seq()
            A = info_dict['A']
            G = info_dict['G']
            C = info_dict['C']
            T = info_dict['T']
            print('Gene:', gene)
            print('Description:', response_dict['desc'])
            print('Total length:', sequence.len())
            print(f"""A {A[0]} ({A[1]})
    C {C[0]} ({C[1]}%)
    G {G[0]} ({G[1]}%)
    T {T[0]} ({T[1]}%)""")
            bases_dict = {'G': G[0], 'A': A[0], 'C': C[0], 'T': T[0]}
            max_value = max(bases_dict, key=bases_dict.get)
            print('Most common base is:', max_value)
    except KeyError:
        print('The gene is not inside our dictionary, Choose one of the following. ', list(DICT_GENES.keys()))