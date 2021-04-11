def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    print_colored("PRINT Command", "green")

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())