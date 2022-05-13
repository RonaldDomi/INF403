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

def select_auteur_ids(conn):
    '''returns all ids of all autheurs as a list of ints'''
    res = []
    
    cur = conn.cursor()   
    
    cur.execute("SELECT numero FROM Auteurs")
    rows = cur.fetchall()
    for row in rows:
        res.append(row[0])     
    
    return res

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

def select_current_auteur_hist(conn):
    """
    Affiche la liste de tous les oeuvres d'un auteurs.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM OeuvreAudios")

    rows = cur.fetchall()

    for row in rows:
        print(row)