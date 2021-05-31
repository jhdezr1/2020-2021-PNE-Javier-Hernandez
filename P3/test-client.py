from Client0 import Client
import socket

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
print(c.talk("PING"))

#get
print("* Testing GET...")
for argument in range(5):
    print('GET', argument, ':', list_sequences[int(argument)])

#info
print("* Testing INFO...")

print(c.talk("INFO ACGTAAAAGTTTAAGCGCCAAT"))


#conp
print('* Testing COMP...')

print(c.talk("COMP ACGTAAAAGTTTAAGCGCCAAT"))


#rev
print('* Testing REV...')

print(c.talk("REV ACGTAAAAGTTTAAGCGCCAAT"))


#gene
print('* Testing GENE...')
print('GENE U5')
print(c.talk("GENE U5"))
print('GENE ADA')
print(c.talk("GENE ADA"))
print('GENE FRAT1')
print(c.talk("GENE FRAT1"))
print('GENE FXN')
print(c.talk("GENE FXN"))
print('GENE RNU6_269P')
print(c.talk("GENE RNU6_269P"))
