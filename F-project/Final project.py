import http.server
import http.client
import socketserver
import termcolor
import pathlib
import jinja2
import json
from urllib.parse import urlparse, parse_qs

PORT = 8081
SERVER = "rest.ensembl.org"
ENDPOINT1 = '/info/species'
ENDPOINT2 = '/info/assembly/'
# between endpoint2 and parameters2 add the species (but not the display name that i did in the first exercise)
PARAMETERS2 = '?bands=1&content-type=application/json'
PARAMETERS1 = '?content-type=application/json'


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

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
        connection = http.client.HTTPConnection(SERVER)
        # connect with the first endpoint
        connection.request('GET', ENDPOINT1 + PARAMETERS1)
        response = connection.getresponse()
        # getting the dictionary
        response_dict = json.loads(response.read().decode())
        # putting all of the species into one list
        species_full = response_dict['species']
        species_name = []
        if path_name == '/':
            contents = read_template_html_file('./html/index.html').render()
        elif path_name == '/listSpecies':
            for e in species_full:
                species_name.append(e['display_name'])
            if 'limit' not in arguments:
                context['length'] = len(species_name)
                context['list_species'] = species_name
                contents = read_template_html_file('./html/list_lim_no.html').render(context=context)
            else:
                if int(arguments['limit'][0]) <= len(species_name):
                    context['length'] = len(species_name)
                    context['list_species'] = species_name
                    context['limit'] = int(arguments['limit'][0])
                    contents = read_template_html_file('./html/list_species.html').render(context=context)
                else:
                    contents = read_template_html_file('./html/ERROR.html').render()
        elif path_name == '/karyotype':
            species_input = arguments['specie'][0]
            connection.request('GET', ENDPOINT2 + species_input + PARAMETERS2)
            response = connection.getresponse()
            # getting the dictionary
            response_dict = json.loads(response.read().decode())
            karyotype_list = response_dict['karyotype']
            context = {
                'karyotype_list': karyotype_list
            }
            contents = read_template_html_file('./html/karyotype.html').render(context=context)
        elif path_name == '/chromosomeLength':
            if 'specie' not in arguments:
                contents = read_template_html_file('./html/ERROR.html').render()
            elif 'chromo' not in arguments:
                contents = read_template_html_file('./html/ERROR.html').render()
            else:
                species_input = arguments['specie'][0]
                chromo_input = arguments['chromo'][0]
                connection.request('GET', ENDPOINT2 + species_input + PARAMETERS2)
                response = connection.getresponse()
                # getting the dictionary
                response_dict = json.loads(response.read().decode())
                for e in response_dict['top_level_region']:
                    if e['name'] == chromo_input and e['coord_system'] == 'chromosome':
                        length_chromo = e['length']

                    else:
                        contents = read_template_html_file('./html/ERROR.html').render()
                context = {
                    'length_chromo': length_chromo
                }
                contents = read_template_html_file('./html/length.html').render(context=context)
        else:
            contents = read_template_html_file('./html/ERROR.html').render()
        print(contents)
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