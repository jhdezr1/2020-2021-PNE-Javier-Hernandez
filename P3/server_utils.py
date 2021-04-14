import termcolor
import colorama
from Seq1 import Seq
def print_colored(message, color):
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    return termcolor.cprint(message, color)
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    termcolor.cprint("PING Command!", "green")
    print('OK!')
def get(cs, list_sequences, argument):
    termcolor.cprint("GET", "yellow")
    response = list_sequences[int(argument)] + '\n'
    print(response)
    cs.send(response.encode())
def info_send(cs, argument):
    s = Seq(argument)
    info_dict = s.info_seq()
    response1 = 'Total length: ' + str(len(argument)) + '\n'
    cs.send(response1.encode())
    response2 = 'A: ' + str(info_dict['A'][0]) + ' ' + str(info_dict['A'][1]) + '%' + '\n'
    cs.send(response2.encode())
    response3 = 'C: ' + str(info_dict['C'][0]) + ' ' + str(info_dict['C'][1]) + '%' + '\n'
    cs.send(response3.encode())
    response4 = 'G: ' + str(info_dict['G'][0]) + ' ' + str(info_dict['G'][1]) + '%' + '\n'
    cs.send(response4.encode())
    response5 = 'T: ' + str(info_dict['T'][0]) + ' ' + str(info_dict['T'][1]) + '%' + '\n'
    cs.send(response5.encode())