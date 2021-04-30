import http.server
import socketserver
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs
import server_utils as su


# Define the Server's port
PORT = 8081

LIST_SEQUENCES = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]

LIST_GENES = ['ADA', 'FRAT1', 'FNX', 'RNU6_269P', 'U5']
BASES_INFORMATION = {
    'A': {'link': "https://en.wikipedia.org/wiki/Adenine",
          'formula': "C5H5NH",
          'name': "ADENINE",
          'colour': 'lightgreen'
    },
    'C': {'link': "https://en.wikipedia.org/wiki/Cytosine",
          'formula': "C4H5N3O",
          'name': "CYTOSINE",
          'colour': 'yellow'
    },
    'G': {'link': "https://en.wikipedia.org/wiki/Guanine",
          'formula': "C5H5N5O",
          'name': "GUANINE",
          'colour': 'lightblue'
    },
    'T': {'link': "https://en.wikipedia.org/wiki/Thymine",
          'formula': "C5H6N2O2",
          'name': "TYROSINE",
          'colour': 'pink'
    }
}

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
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
        if path_name == '/':
            context['n_sequences'] = len(LIST_SEQUENCES)
            context['list_genes'] = LIST_GENES
            contents = su.read_template_html_file('./html/index.html').render(context=context)
        elif path_name == '/test':
            contents = su.read_template_html_file('./html/test.html').render()
        elif path_name == '/ping':
            contents = su.read_template_html_file('./html/ping.html').render()
        elif path_name == '/get':
            number_sequence = arguments['sequence'][0]
            contents = su.get(LIST_SEQUENCES, number_sequence)
        elif path_name == '/gene':
            gene = arguments['gene'][0]
            contents = su.gene(gene)
        elif path_name == '/operation':
            sequence = arguments['sequence'][0]
            calculation = arguments['calculation'][0]
            if calculation == 'Info':
                contents = su.info(sequence)
            elif calculation == 'Comp':
                contents = su.comp(sequence)
            elif calculation == 'Rev':
                contents = su.rev(sequence)
            else:
                contents = su.read_template_html_file('./html/error.html').render()
        else:
            contents = su.read_template_html_file('./html/error.html').render()


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