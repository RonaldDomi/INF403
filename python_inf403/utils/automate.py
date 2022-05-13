
from doctest import ELLIPSIS_MARKER
from utils.screen_helpers import *
from utils.states import *
from utils.sql_helpers import *

current_client = 0
current_auteur = 0

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
            parameter = ''

    return raw, parameter
    
def handle_action(conn, current_state, usr_input, parameter):
    '''
    menage actions on inputs\n
    states not considered: information, help, 
    auteurs, clients, types, oeuvres.
    '''
    global current_client
    global current_auteur
    
    if(current_state == states['start']):
        print_introduction()
    elif(current_state == states['main']):
        if (usr_input == 'help' or usr_input == '-h'):
            print_help()
        elif (usr_input == 'description' or usr_input == '-d'):
            print_description()
        elif (usr_input == 'information' or usr_input == '-i'):
            print_information()
        elif (usr_input == 'connect' or usr_input == '-c'):
            param = {
                "username" : "zeynel",
                "id" : 100,
                "date" : '23-02-2001'
            }
            if should_connect_client(parameter, conn):
                obj = get_client(conn, parameter)
                print_welcome_client(obj)
                current_client = parameter 
            elif should_connect_auteur(parameter, conn):
                obj = get_auteur(conn, parameter)
                current_auteur = parameter 
                print_welcome_auteur(obj)
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
            if should_shop_client(parameter, conn):
                insert_into_possede(conn, current_client, parameter)
                print('Thank you for buying our product')
            else:
                print("Didn't purchase: id entered not found")
        elif (usr_input == 'history' or usr_input == '--hist'):
            select_current_client_history(conn, current_client)
    elif(current_state == states['connect_auteur']):
        if (usr_input == 'history' or usr_input == '--hist'):
            select_current_auteur_history(conn, current_auteur)
        elif(usr_input == "sell"):
            return_obj = input_oeuvre()
            insert_into_oeuvres(conn, return_obj)
        elif(usr_input == "remove"):
            if should_remove_auteur(conn, current_auteur, parameter):
                remove_oeuvre(conn, parameter)
            else:
                print("You cannot remove that item")
        elif(usr_input == 'stat'):
            select_current_author_stat(conn, current_auteur)

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
            # --help --description
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
        else:
            return states['connect_client']
    elif(current_state == states['connect_auteur']):
        if(usr_input == 'main'):
            return states['main']    
        elif(usr_input == 'quit'):
            return states['final_state']  
        else:
            return states['connect_auteur']
