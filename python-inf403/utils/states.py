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
    "connect": 10,
    "buy": 11,
    "history_client": 12,
    "sell": 13,
    "history_auteur": 14,
    "final_state": 100
}

#commands available for each of the states in the automate
states_commands = {
    0: [], #start
    1: [], #intro
    2: ['--help', '--description', '--information'], #main
    3: [], #description
    4: [], #help
    5: ['auteurs', 'clients'], #information
    6: [], #info_auteur
    7: [], #info_type
    8: [], #info_clients
    9: [], #info_oeuvre
    10: [], #connect
    11: [], #buy
    12: [], #history_client
    13: [], #sell
    14: [], #history_auteur
    100: [],
}
