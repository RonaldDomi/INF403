#!/usr/bin/python3

from utils import db
from utils.automate import *


def main():

    # Nom de la BD à créer
    db_file = "data/project.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("On crée la bd et on l'initialise avec des premières valeurs.\n")
    db.mise_a_jour_bd(conn, "data/creation.sql")
    db.mise_a_jour_bd(conn, "data/insert.sql")

    # Lire la BD
    # print("2. Liste de tous les Auteurs")
    # select_tous_les_auteurs(conn)
    start_automate(conn)



if __name__ == "__main__":
    main()
