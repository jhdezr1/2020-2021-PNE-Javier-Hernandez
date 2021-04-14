from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 1202

c = Client(IP, PORT)
print(c)

#ping
print("* Testing PING...")
print(c.talk("OK!"))

#get
print("* Testing GET...")
for argument in range(5):
    list_sequences[int(argument)] + '\n'
    pass
