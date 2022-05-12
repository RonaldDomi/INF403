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
