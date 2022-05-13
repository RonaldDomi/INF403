states = {
    "start": 0,
    "intro": 1, 
    "main": 2,
    "description": 3,
    "help": 4,
    "information": 5,
    "info_auteur": 6,
    "info_type": 7,
    "info_clients": 8,
    "info_oeuvre": 9,
    "connect ": 10,
    "buy": 11,
    "history_client": 12,
    "sell": 13,
    "history_auteur": 14,
    "final_state": 100
}

#commands available for each of the states in the automate
states_commands = {
    # ------------- empty states
    0: [], #start
    1: [], #intro
    3: [], #description
    4: [], #help
    6: [], #info_auteur
    7: [], #info_type
    8: [], #info_clients
    9: [], #info_oeuvre
    # -----------!! empty states

    2: ['help', '-h', 'description', '-d', 'information', '-i', 'quit', 
        'connect'], #main
    5: ['auteurs', 'clients', 'types', 'oeuvres', 'main', 'quit'], #information
    10: [], #connect_user
    11: [], #buy
    12: [], #history_client
    13: [], #connect_auteur
    14: [], #sell
    15: [], #history_auteur
    100: [],
}
