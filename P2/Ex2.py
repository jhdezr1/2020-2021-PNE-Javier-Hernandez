from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f'------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE} |--------')

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
print(c)