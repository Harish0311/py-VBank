from os import system, name

def clearConsole():
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux
    else:
        system('clear')