from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

print(c)

# -- Send a message to the server
c.debug_talk("This is a trial number 1")
c.debug_talk("This is a trial number 2")