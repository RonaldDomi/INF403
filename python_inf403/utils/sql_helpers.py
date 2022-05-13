def select_tous_les_auteurs(conn):
    """
    Affiche la liste de tous les auteurs.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Auteurs")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_tous_les_clients(conn):
    """
    Affiche la liste de tous les clients.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clients")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_tous_les_types(conn):
    """
    Affiche la liste de tous les types.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Audio_Types")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_tous_les_oeuvres(conn):
    """
    Affiche la liste de tous les oeuvres.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM OeuvreAudios")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_client_ids(conn):
    '''returns all ids of all clients as a list of ints'''
    res = []
    
    cur = conn.cursor()
    
    cur.execute("SELECT numero FROM Clients")
    rows = cur.fetchall()
    for row in rows:
        res.append(row[0])     
    
    return res

def select_oeuvre_ids(conn):
    '''returns all ids of all oeuvres as a list of ints'''
    res = []
    
    cur = conn.cursor()
    
    cur.execute("SELECT numero FROM OeuvreAudios")
    rows = cur.fetchall()
    for row in rows:
        res.append(row[0])     
    
    return res

def select_auteur_ids(conn):
    '''returns all ids of all autheurs as a list of ints'''
    res = []
    
    cur = conn.cursor()   
    
    cur.execute("SELECT numero FROM Auteurs")
    rows = cur.fetchall()
    for row in rows:
        res.append(row[0])     
    
    return res

def select_current_auteur_history(conn, id):
    '''return the history of possisions of the current auteur'''
    res = []
    
    cur = conn.cursor()   
    sql_string = "SELECT * FROM Ecrit WHERE auteur_numero = " + str(id)
    cur.execute(sql_string)
    
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_current_client_history(conn, id):
    '''return the history of possisions of the current client'''
    res = []
    
    cur = conn.cursor()   
    sql_string = "SELECT * FROM Possede WHERE client_numero = " + str(id)
    cur.execute(sql_string)
    
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_auteur_oeuvres(id, conn):
    '''return all oeuvres written by id auteur'''
    res = []
    
    cur = conn.cursor()   
    sql_string = "SELECT * FROM Ecrit WHERE auteur_numero = " + str(id)
    cur.execute(sql_string)
    
    
    rows = cur.fetchall()
    for row in rows:
        res.append(row[1])

    return res

def insert_into_possede(conn, client_id, oeuvre_id):
    '''insert into possede (client_id, oeuvre_id)'''
    cur = conn.cursor()   
    sql_string = "INSERT INTO Possede VALUES (" + str(client_id) + ', ' + str(oeuvre_id) + ')'
    cur.execute(sql_string)


def insert_into_oeuvres(conn, obj):
    '''insert into oeuvre '''
    cur = conn.cursor()   
    sql_string = 'INSERT INTO OeuvreAudios VALUES (' + \
                      obj["id"] + ', ' + obj["name"] + ',' + obj["prix"] + ',' + obj["type"] + ')'
    cur.execute(sql_string)
    

def remove_oeuvre(conn, id):
    '''removes from oeuvres'''
    cur = conn.cursor()   
    sql_string = 'DELETE FROM OeuvreAudios WHERE numero = ' + str(id)
    cur.execute(sql_string)
    

def should_connect_client(id, conn):
    '''id is expected to be an int, and it returs if we 
    did connect or not'''
    all_ids = select_client_ids(conn)

    if(id in all_ids):
        return True 
    return False
    
def should_connect_auteur(id, conn):
    '''id is expected to be an int, and it returs if we 
    did connect or not'''
    all_ids = select_auteur_ids(conn)

    if(id in all_ids):
        return True 
    return False

def should_shop_client(id, conn):
    '''id is expected to be an int, and it returs if can buy the thing'''
    all_ids = select_oeuvre_ids(conn)

    if(id in all_ids):
        return True 
    return False


def should_remove_auteur(conn, auteur_id, oeuvre_id):
    '''id is expected to be an int, and it returs if we could remove that title'''
    all_ids = select_auteur_oeuvres(auteur_id, conn)

    if(oeuvre_id in all_ids):
        return True 
    return False

def get_client(conn, id):
    '''return client data'''
    res = []
    cur = conn.cursor()   
    sql_string = "SELECT * FROM Clients WHERE numero = " + str(id)
    cur.execute(sql_string)
    
    
    rows = cur.fetchall()
    data = rows[0]
    param = {
        "username" : data[1],
        "id" : data[0]
    }

    return param

def get_auteur(conn, id):
    '''return auteur data'''
    res = []
    cur = conn.cursor()   
    sql_string = "SELECT * FROM Auteurs WHERE numero = " + str(id)
    cur.execute(sql_string)
    
    rows = cur.fetchall()
    data = rows[0]
    param = {
        "username" : data[1],
        "id" : data[0]
    }

    return param