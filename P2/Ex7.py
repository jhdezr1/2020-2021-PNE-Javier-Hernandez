from Client0 import Client
import socket
from pathlib import Path
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 7

print(f'------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE} |--------')

IP = "127.0.0.1"
PORT = 12000
PORT_2 = 12001
s1 = Seq()
s1.read_fasta('./FRAT1.txt')
count = 0
i = 0
while i < len(s1.strbases) and count < 10:
    fragment = s1.strbases[i: i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    if count % 2 == 0:
        s_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_2.connect((IP, PORT_2))
        s_2.send(('Fragment ' + str(count) + ' : ' + fragment + '\n').encode())
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(('Fragment ' + str(count) + ' : ' + fragment + '\n').encode())