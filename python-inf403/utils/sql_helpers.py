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


def select_all_ids(conn):
    '''returns all ids of all clients and autheurs as a list of ints'''
    cur = conn.cursor()
    cur.execute("SELECT numero FROM OeuvreAudios")

    rows = cur.fetchall()
    print(rows)