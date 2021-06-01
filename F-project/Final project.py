import http.server
import http.client
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
import json
PORT = 8081

DICT_GENES_ID = {
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

ENDPOINT1 = '/info/species'
ENDPOINT2 = '/info/assembly/'
ENDPOINT3 = '/sequence/id/'


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print('Resource requested: ', path_name)
        print('Parameters: ', arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        context = {}
        response_dict = su.get_dict(ENDPOINT1)
        # putting all of the species into one list
        species_full = response_dict['species']
        species_name = []
        if path_name == '/':
            context = {

            }
            if 'json' in arguments:
                if arguments['json'][0] == '1':
                    contents = json.dumps(context)
                    content_type = 'application/json'
                    error_code = 200
                else:
                    contents = su.read_template_html_file('./html/ERROR.html').render()
                    content_type = 'text/html'
                    error_code = 404
            else:
                contents = su.read_template_html_file('./html/index.html').render()
                content_type = 'text/html'
                error_code = 200
        elif path_name == '/listSpecies':
            try:
                for e in species_full:
                    species_name.append(e['display_name'])
                if 'limit' not in arguments:
                    context['length'] = len(species_name)
                    context['list_species'] = species_name
                    if 'json' in arguments:
                        if arguments['json'][0] == '1':
                            contents = json.dumps(context)
                            content_type = 'application/json'
                            error_code = 200
                        else:
                            contents = su.read_template_html_file('./html/ERROR.html').render()
                            content_type = 'text/html'
                            error_code = 404
                    else:
                        contents = su.read_template_html_file('./html/list_lim_no.html').render(context=context)
                        content_type = 'text/html'
                        error_code = 200
                else:
                    if int(arguments['limit'][0]) <= len(species_name):
                        context['length'] = len(species_name)
                        context['list_species'] = species_name
                        context['limit'] = int(arguments['limit'][0])
                        if 'json' in arguments:
                            if arguments['json'][0] == '1':
                                context['list_species'] = []
                                for e in range(0, int(arguments['limit'][0])):
                                    context['list_species'].append(species_name[e])
                                contents = json.dumps(context)
                                content_type = 'application/json'
                                error_code = 200
                            else:
                                contents = su.read_template_html_file('./html/ERROR.html').render()
                                content_type = 'text/html'
                                error_code = 404
                        else:
                            contents = su.read_template_html_file('./html/list_species.html').render(context=context)
                            content_type = 'text/html'
                            error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        elif path_name == '/karyotype':
            try:
                if 'json' not in arguments:
                    species_input = arguments['specie'][0]
                    response_dict = su.get_dict(ENDPOINT2 + species_input)
                    karyotype_list = response_dict['karyotype']
                    context = {
                        'karyotype_list': karyotype_list
                    }
                    contents = su.read_template_html_file('./html/karyotype.html').render(context=context)
                    content_type = 'text/html'
                    error_code = 200
                else:
                    if arguments['json'][0] == '1':
                        species_input = arguments['specie'][0]
                        response_dict = su.get_dict(ENDPOINT2 + species_input)
                        karyotype_list = response_dict['karyotype']
                        context = {
                            'karyotype_list': karyotype_list
                        }
                        contents = json.dumps(context)
                        content_type = 'application/json'
                        error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        elif path_name == '/chromosomeLength':
            try:
                if 'json' in arguments:
                    if arguments['json'][0] == '1':
                        if 'specie' not in arguments:
                            contents = su.read_template_html_file('./html/ERROR.html').render()
                            content_type = 'text/html'
                            error_code = 404
                        elif 'chromo' not in arguments:
                            contents = su.read_template_html_file('./html/ERROR.html').render()
                            content_type = 'text/html'
                            error_code = 404
                        else:
                            species_input = arguments['specie'][0]
                            chromo_input = arguments['chromo'][0]
                            response_dict = su.get_dict(ENDPOINT2 + species_input)
                            for e in response_dict['top_level_region']:
                                if e['name'] == chromo_input and e['coord_system'] == 'chromosome':
                                    length_chromo = e['length']

                                else:
                                    contents = su.read_template_html_file('./html/ERROR.html').render()
                                    content_type = 'text/html'
                                    error_code = 404
                            context = {
                                'length_chromo': length_chromo
                            }
                            contents = json.dumps(context)
                            content_type = 'application/json'
                            error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                else:
                    if 'specie' not in arguments:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                    elif 'chromo' not in arguments:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                    else:
                        species_input = arguments['specie'][0]
                        chromo_input = arguments['chromo'][0]
                        response_dict = su.get_dict(ENDPOINT2 + species_input)
                        for e in response_dict['top_level_region']:
                            if e['name'] == chromo_input and e['coord_system'] == 'chromosome':
                                length_chromo = e['length']

                            else:
                                contents = su.read_template_html_file('./html/ERROR.html').render()
                                content_type = 'text/html'
                                error_code = 404
                        context = {
                            'length_chromo': length_chromo
                        }
                        contents = su.read_template_html_file('./html/length.html').render(context=context)
                        content_type = 'text/html'
                        error_code = 200
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        elif path_name == '/geneSeq':
            try:
                if 'json' in arguments:
                    if arguments['json'][0] == '1':
                        gene_ask = arguments['gene'][0]
                        id_gene = DICT_GENES_ID[gene_ask]
                        response_dict = su.get_dict(ENDPOINT3 + id_gene)
                        sequence_asked = response_dict['seq']
                        context = {
                            'sequence': sequence_asked,
                            'gene': gene_ask
                        }
                        contents = json.dumps(context)
                        content_type = 'application/json'
                        error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                else:
                    gene_ask = arguments['gene'][0]
                    id_gene = DICT_GENES_ID[gene_ask]
                    response_dict = su.get_dict(ENDPOINT3 + id_gene)
                    sequence_asked = response_dict['seq']
                    context = {
                        'sequence': sequence_asked,
                        'gene': gene_ask
                    }
                    contents = su.read_template_html_file('./html/geneSeq.html').render(context=context)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        elif path_name == '/geneInfo':
            try:
                gene_ask = arguments['gene'][0]
                id_gene = DICT_GENES_ID[gene_ask]
                response_dict = su.get_dict(ENDPOINT3 + id_gene)
                chromosome_info_list = response_dict['desc'].split(':')
                name_chromosome = chromosome_info_list[1]
                number_chromosome =  chromosome_info_list[2]
                start_coordinates =  chromosome_info_list[3]
                end_coordinates =  chromosome_info_list[4]
                lists_info = su.get_list_info(response_dict)
                context = {
                    'name_chromosome' : name_chromosome,
                    'number_chromosome': number_chromosome,
                    'start_coordinates': start_coordinates,
                    'end_coordinates': end_coordinates,
                    'id': id_gene,
                    'length_gene': lists_info[4],
                    'gene': gene_ask
                }
                if 'json' in arguments:
                    if arguments['json'][0] == '1':
                        contents = json.dumps(context)
                        content_type = 'application/json'
                        error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                else:
                    contents = su.read_template_html_file('./html/geneInfo.html').render(context=context)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        elif path_name == '/geneCalc':
            try:
                gene_ask = arguments['gene'][0]
                id_gene = DICT_GENES_ID[gene_ask]
                response_dict = su.get_dict(ENDPOINT3 + id_gene)
                lists_info = su.get_list_info(response_dict)
                context = {
                    'gene': gene_ask,
                    'length': lists_info[4],
                    'A': lists_info[0],
                    'G': lists_info[2],
                    'C': lists_info[1],
                    'T': lists_info[3]
                }
                if 'json' in arguments:
                    if arguments['json'][0] == '1':
                        contents = json.dumps(context)
                        content_type = 'application/json'
                        error_code = 200
                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                        content_type = 'text/html'
                        error_code = 404
                else:
                    contents = su.read_template_html_file('./html/geneCalc.html').render(context=context)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
                content_type = 'text/html'
                error_code = 404
        else:
            contents = su.read_template_html_file('./html/ERROR.html').render()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()