states = {
    "start": 0,
    "main": 1,
    "information": 2,
    "connect_client": 3,
    "connect_auteur": 4,
}

#commands available for each of the states in the automate
states_commands = {
    #main
    1: ['help', '-h', 
        'description', '-d', 
        'information', '-i', 
        'connect', '-c'
        'quit', 
        ], 
    #information
    2: ['auteurs', 'clients', 'types', 'oeuvres', 
        'main', 'quit'
        ],
    #connect client
    3: ['history', '--hist', 
        'buy', 
        'main', 'quit'
        ], 
    #connect auteur
    4: ['history', '--hist',  
        'create', 
        'delete', 
        'statistics', '-s'
        'main', 'quit' 
        ],
}
