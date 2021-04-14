import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
(cs, client_ip_port) = ls.accept()

print("A client has connected to the server!")

# -- Read the message from the client
# -- The received message is in raw bytes
msg_raw = cs.recv(2048)

# -- We decode it for converting it
# -- into a human-redeable string
msg = msg_raw.decode()

# -- Print the received message
print(f"Received Message: {msg}")

# -- Send a response message to the client
response = "HELLO. I am the Happy Server :-)\n"

# -- The message has to be encoded into bytes
cs.send(response.encode())

# -- Close the client socket
cs.close()
# -- Close the socket
ls.close()

print("A client has connected to the server!")

# -- Close the socket
ls.close()