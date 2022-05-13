
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
    #parametred commands
    if(len(raw.split(' ')) > 1):
        print('space seen')
        items = raw.split(' ')
        if(items[0] == 'connect' 
           and 'connect' in states_commands[current_state] and items.length == 2):
            id = int(items[1])
            all_ids = select_all_ids()

    #normal commands
    while raw not in states_commands[current_state]:
        print("Command not recognized!")
        print("Commands available: ", states_commands[current_state])
        raw = input("Enter next command: ")
    return raw
    
def handle_action(conn, current_state, usr_input):
    '''
    menage actions on inputs\n
    states not considered: information, help, 
    auteurs, clients, types, oeuvres.
    '''
    
    if(current_state == states['start']):
        print_introduction()
    elif(current_state == states['main']):
        if (usr_input == 'help' or usr_input == '-h'):
            print_help()
        elif (usr_input == 'description' or usr_input == '-d'):
            print_description()
        elif (usr_input == 'information' or usr_input == '-i'):
            print_information()
        elif (usr_input == 'quit'):
            print_quit()


    elif(current_state == states['information']):
        if (usr_input == 'auteurs'):
            select_tous_les_auteurs(conn)
        elif (usr_input == 'clients'):
            select_tous_les_clients(conn)
        elif (usr_input == 'types'):
            select_tous_les_types(conn)
        elif (usr_input == 'oeuvres'):
            select_tous_les_oeuvres(conn)

def transition(current_state, usr_input):
    '''
    transition for states which can accept input\n
    states not considered: information, help, 
    auteurs, clients, types, oeuvres.
    '''
    if(current_state == states['start']):
        return states['main']
    elif(current_state == states['main']):
        if(usr_input == 'help' or usr_input == '-h'):
            # go to states['information'] and return to main
            return states['main']
        elif(usr_input == 'description' or usr_input == '-d'):
            return states['main']
        elif(usr_input == 'information' or usr_input == '-i'):
            return states['information']    
        elif(usr_input == 'quit'):
            return states['final_state']    
    elif(current_state == states['information']):
        if(usr_input == 'auteurs' or 
          usr_input == 'clients' or
          usr_input == 'types' or
          usr_input == 'oevres'
          ):
            return states['information']
        elif(usr_input == 'main'):
            return states['main']    
        elif(usr_input == 'quit'):
            return states['final_state']    

