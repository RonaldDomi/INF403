
from doctest import ELLIPSIS_MARKER
from utils.screen_helpers import *
from utils.states import *
from utils.sql_helpers import *


def start_automate(conn):
    '''
    This is the program loop
    '''
    current_state = states['start']
    while current_state != states["final_state"]:
        usr_input, parameter = get_input(current_state)
        next_state = transition(conn, current_state, usr_input, parameter)
        handle_action(conn, current_state, usr_input, parameter)
        current_state = next_state
    

def get_input(current_state):
    if(current_state == states['start']):
        return None, None
            
    parameter = ''
    #normal commands
    # if(parameter.isalpha()):
    #     print("parameter is alpha")
    
    condition = True
    while condition:
        raw = input("Enter next command: ")
        
        # test for number of parameters
        err_arguments = False
        if(len(raw.split(' ')) == 2):
            items = raw.split(' ')
            raw = items[0]
            parameter = items[1]
        elif(len(raw.split(' ')) > 2):
            err_arguments = True

        # if correct number of parameters
        if not err_arguments:
            condition = raw not in states_commands[current_state]
            if(parameter.isnumeric()):
                parameter = int(parameter)

        if(condition):
            print("Command not recognized!")
            print("Commands available: ", states_commands[current_state])
            
    return raw, parameter
    
def handle_action(conn, current_state, usr_input, parameter):
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
        elif (usr_input == 'connect'):
            if should_connect_client(parameter, conn):
                print_welcome_client()
            elif should_connect_auteur(parameter, conn):
                print_welcome_auteur()
            else:
                print("Didn't connect: id entered not found")

        # elif (usr_input == 'quit'):
        #     print_quit()


    elif(current_state == states['information']):
        if (usr_input == 'auteurs'):
            select_tous_les_auteurs(conn)
        elif (usr_input == 'clients'):
            select_tous_les_clients(conn)
        elif (usr_input == 'types'):
            select_tous_les_types(conn)
        elif (usr_input == 'oeuvres'):
            select_tous_les_oeuvres(conn)
    
    elif(current_state == states['connect_client']):
        if (usr_input == 'shop'):
            print("shop")
        if (usr_input == 'history'):
            print("history")
    elif(current_state == states['connect_auteur']):
        pass
        # if (usr_input == 'shop'):
        #     print("shop")
        # if (usr_input == 'history'):
        #     print("history")

def transition(conn, current_state, usr_input, parameter):
    '''
    transition for states which can accept input\n
    states not considered: information, help, 
    auteurs, clients, types, oeuvres, is_connecting.
    '''
    if(current_state == states['start']):
        return states['main']
    elif(current_state == states['main']):
        if(usr_input == 'information' or usr_input == '-i'):
            return states['information']    
        elif(usr_input == 'connect'):
            if should_connect_client(parameter, conn):    
                return states['connect_client']
            elif should_connect_auteur(parameter, conn):
                return states['connect_auteur']
            else:
                return states['main']
        elif(usr_input == 'quit'):
            return states['final_state']  
        else:
            #sinon on revient
            return states['main']
    elif(current_state == states['information']):
        if(usr_input == 'main'):
            return states['main']    
        elif(usr_input == 'quit'):
            return states['final_state']    
        else:
            return states['information']
    
    elif(current_state == states['connect_client']):
        if(usr_input == 'main'):
            return states['main']    
        elif(usr_input == 'quit'):
            return states['final_state']   
    elif(current_state == states['connect_auteur']):
        if(usr_input == 'main'):
            return states['main']    
        elif(usr_input == 'quit'):
            return states['final_state']   
        # if(usr_input == 'main'):
        #     return states['main']    

