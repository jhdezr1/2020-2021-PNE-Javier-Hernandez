import socket
import server_utils


list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 1202
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
count = +1

print("The server is configured!")
client_address_list = []
count_connections = 0

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept() #count connections always after accept
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ".Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        formatted_message = server_utils.format_command(msg)
        formatted_message = formatted_message.split(" ")
        if len(formatted_message) == 1:
            command = formatted_message[0]
        else:
            command =formatted_message[0]
            argument = formatted_message[1]

        if command == "PING":
            response = 'OK!\n'
            server_utils.ping()
            # -- The message has to be encoded into bytes
            cs.send(response.encode())
        if command == 'GET':
            if argument == '0':
                server_utils.get(cs, list_sequences, 0)
            elif argument == '1':
                server_utils.get(cs, list_sequences, 1)
            elif argument == '2':
                server_utils.get(cs, list_sequences, 2)
            elif argument == '3':
                server_utils.get(cs, list_sequences, 3)
            elif argument == '4':
                server_utils.get(cs, list_sequences, 4)
        if command == 'INFO':
            server_utils.info_send(cs, argument)
        if command == 'COMP':
            server_utils.comp_send(cs, argument)
        if command == 'REV':
            server_utils.rev_send(cs, argument)
        if command == 'GENE':
            server_utils.gene_send(cs, argument)

        # -- Send a response message to the client
        #try is used to avoid the server to stop when something not transformable into an integer is introduced
            #response = "OK!"
        # -- The message has to be encoded into bytes
            #cs.send(str(response).encode()) # the int is back to a str and encoded into bytes by .encode and sent back to client

        #else:
           # response = "Not available command"
            #cs.send(str(response).encode())
        # -- Close the data socket
        cs.close()