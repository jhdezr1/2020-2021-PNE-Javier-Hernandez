import socket
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print('Ok')

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print('Server is up')
            s.close()
        except ConnectionRefusedError:
            print('Could not connect to the server, Is it running? HAve you checked the port and the IP?')

    def __str__(self):
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((self.ip, self.port))
        return 'Connection to SERVER at ' + self.ip + ', PORT: ' + str(self.port)
    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print(msg)
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return response
    def debug_talk(self, msg):
        response = self.talk(msg)
        colored_response = colored(response, 'green')
        print("From Server:", colored_response)

