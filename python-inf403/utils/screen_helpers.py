from utils.automate import *


def print_introduction():
    print("--------Introduction-------------")

    
def print_description():
    print("--------Description-------------")

    
def print_help():
    print("--------Help-------------")

    
def print_information():
    print("--------Information-------------")

def print_falseCommand():
    print("Command not recognized!")

def print_availableCommand(current_state):
    print("Commands available: ", states_commands[current_state])