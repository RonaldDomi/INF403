
from utils.screen_helpers import *
from utils.states import *
from utils.sql_helpers import *


def start_automate(conn):
    '''
    This is the program loop
    '''
    current_state = states['start']
    while current_state != states["final_state"]:
        usr_input = get_input(current_state)
        next_state = transition(current_state, usr_input)
        handle_action(conn, current_state, usr_input)
        current_state = next_state
    

def get_input(current_state):
    if(current_state == states['start']):
        return
    raw = input("Enter next command: ")
    print()
    while raw not in states_commands[current_state]:
        print("Command not recognized!")
        print("Commands available: ", states_commands[current_state])
        raw = input("Enter next command: ")
    return raw
    
def handle_action(conn, current_state, usr_input):
    if(current_state == states['start']):
        print_introduction()
    elif(current_state == states['main']):
        if (usr_input == '--help'):
            print_help()
        elif (usr_input == '--description'):
            print_description()
        elif (usr_input == '--information'):
            print_information()


    elif(current_state == states['help']):
        # could never be in this state
        pass
    elif(current_state == states['description']):
        # could never be in this state
        pass
    elif(current_state == states['information']):
        if (usr_input == 'auteurs'):
            select_tous_les_auteurs(conn)
        elif (usr_input == 'clients'):
            select_tous_les_clients(conn)

def transition(current_state, usr_input):
    if(current_state == states['start']):
        return states['main']
    elif(current_state == states['main']):
        if(usr_input == '--help' or usr_input == '-h'):
            # go to states['information'] and return to main
            return states['main']
        elif(usr_input == '--description'):
            return states['main']
        elif(usr_input == '--information'):
            return states['information']
        
    elif(current_state == states['help']):
        #could never be in this state
        pass
    elif(current_state == states['description']):
        #could never be in this state
        pass
    elif(current_state == states['information']):
        if(usr_input == 'auteurs' or usr_input == 'clients'):
            return states['information']

