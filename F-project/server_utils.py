import termcolor
import colorama
from Seq1 import Seq
import jinja2
import pathlib
import http.client
import json
def print_colored(message, color):
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    return termcolor.cprint(message, color)
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    termcolor.cprint("PING Command!", "green")
    print('OK!')
def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)] + '\n'
    context = {
        'number': seq_number,
        'sequence': list_sequences[int(seq_number)]
    }
    contents = read_template_html_file('./html/get.html').render(context=context)
    return contents

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def info(sequence):
    s = Seq(sequence)
    info_dict = s.info_seq()
    response = f"""Total length {len(sequence)}
A: {info_dict['A'][0]} ({info_dict['A'][1]})
C: {info_dict['C'][0]} ({info_dict['C'][1]})
G: {info_dict['A'][0]} ({info_dict['G'][1]})
T: {info_dict['T'][0]} ({info_dict['T'][1]})"""
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'info'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents

def comp(sequence):
    s = Seq(sequence)
    complement = s.complement()
    response = complement + '\n'
    context = {
        'sequence' : sequence,
        'information': response,
        'operation': 'comp'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents

def rev(sequence):
    s = Seq(sequence)
    rev = s.reverse()
    response = rev + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Rev'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents
def gene(seq_name):
    gene_path = './sequences/' + seq_name + '.txt'
    s = Seq()
    s.read_fasta(gene_path)
    context = {
        'gene_name': seq_name,
        'gene_contents': s.strbases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents

def get_dict(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMETERS = '?content-type=application/json'
    connection = http.client.HTTPConnection(SERVER)
    # connect with the first endpoint
    connection.request('GET', ENDPOINT + PARAMETERS)
    response = connection.getresponse()
    # getting the dictionary
    response_dict = json.loads(response.read().decode())
    return response_dict

def get_list_info(dict_info):
    sequence_asked = dict_info['seq']
    seq_seq = Seq(sequence_asked)
    length_seq = []
    length = seq_seq.len()
    length_seq.append(length)
    info_dict = seq_seq.info_seq()
    list_A = info_dict['A']
    list_C = info_dict['C']
    list_G = info_dict['G']
    list_T = info_dict['T']
    lists_info = []
    lists_info.append(list_A)
    lists_info.append(list_C)
    lists_info.append(list_G)
    lists_info.append(list_T)
    lists_info.append(length_seq)
    return lists_info

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


def test_endpoint_json(endpoint):
    conn = http.client.HTTPConnection('localhost', '8081')
    try:
        conn.request("GET", endpoint + '&json=1')
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Print the received data
    return data1