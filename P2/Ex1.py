from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f'------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE} |--------')

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
c.advanced_ping()
c.ping()