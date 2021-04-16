from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]

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

#info
print("* Testing INFO...")

s = c.talk("INFO ACGTAAAAGTTTAAGCGCCAAT")
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
response1 = s.recv(2048).decode("uft-8")
response2 = s.recv(2048).decode("uft-8")
response3 = s.recv(2048).decode("uft-8")
response4 = s.recv(2048).decode("uft-8")
s.close()
print("From server: " + response + '\n' + response1 + '\n' + response2 + '\n'+ response3 + '\n' + response4 + '\n')

#conp
print('* Testing COMP...')

s = c.talk("COMP ACGTAAAAGTTTAAGCGCCAAT")
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)

#rev
print('* Testing REV...')

s = c.talk("REV ACGTAAAAGTTTAAGCGCCAAT")
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)

#gene
print('* Testing GENE...')

s = c.talk("GENE ACGTAAAAGTTTAAGCGCCAAT")
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)