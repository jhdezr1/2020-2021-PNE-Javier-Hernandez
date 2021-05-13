import http.server
import http.client
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su
from Seq1 import Seq

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
            contents = su.read_template_html_file('./html/index.html').render()
        elif path_name == '/listSpecies':
            for e in species_full:
                species_name.append(e['display_name'])
            if 'limit' not in arguments:
                context['length'] = len(species_name)
                context['list_species'] = species_name
                contents = su.read_template_html_file('./html/list_lim_no.html').render(context=context)
            else:
                if int(arguments['limit'][0]) <= len(species_name):
                    context['length'] = len(species_name)
                    context['list_species'] = species_name
                    context['limit'] = int(arguments['limit'][0])
                    contents =su. read_template_html_file('./html/list_species.html').render(context=context)
                else:
                    contents = su.read_template_html_file('./html/ERROR.html').render()
        elif path_name == '/karyotype':
            species_input = arguments['specie'][0]
            response_dict = su.get_dict(ENDPOINT2)
            karyotype_list = response_dict['karyotype']
            context = {
                'karyotype_list': karyotype_list
            }
            contents = su.read_template_html_file('./html/karyotype.html').render(context=context)
        elif path_name == '/chromosomeLength':
            if 'specie' not in arguments:
                contents = su.read_template_html_file('./html/ERROR.html').render()
            elif 'chromo' not in arguments:
                contents = su.read_template_html_file('./html/ERROR.html').render()
            else:
                species_input = arguments['specie'][0]
                chromo_input = arguments['chromo'][0]
                response_dict = su.get_dict(ENDPOINT2 + species_input)
                for e in response_dict['top_level_region']:
                    if e['name'] == chromo_input and e['coord_system'] == 'chromosome':
                        length_chromo = e['length']

                    else:
                        contents = su.read_template_html_file('./html/ERROR.html').render()
                context = {
                    'length_chromo': length_chromo
                }
                contents = su.read_template_html_file('./html/length.html').render(context=context)
        elif path_name == '/geneSeq':
            try:
                gene_ask = arguments['gene'][0]
                id_gene = DICT_GENES_ID[gene_ask]
                response_dict = su.get_dict(ENDPOINT3 + id_gene)
                sequence_asked = response_dict['seq']
                print(sequence_asked)
                context = {
                    'sequence': sequence_asked,
                    'gene': gene_ask
                }
                contents = su.read_template_html_file('./html/geneSeq.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html/ERROR.html').render()
        elif path_name == '/geneCalc':
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
            contents = su.read_template_html_file('./html/geneCalc.html').render(context=context)
        else:
            contents = su.read_template_html_file('./html/ERROR.html').render()

        
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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