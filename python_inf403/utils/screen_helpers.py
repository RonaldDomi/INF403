from utils.automate import *


def print_introduction():
    print("--------Introduction-------------")
    print("\nSonny a constitué une base de données relationnelle sur la plateforme de vente d’audio en ligne.\nSonny représente pour chaque audio identifie par une numéro, le nom et le prix de cette audio.\nChaque audio a un type spécifique, qui peut être podcast, livre audio ou autre en forme de string.\nAvec le type est associe une longueur max qui montre le longueur max que peut avoir l’audio.")
    print("\nLes audios sont créé entièrement ou partiellement(features) par des auteurs.\nPour être un auteur il faut nécessairement avoir crée ou moins une œuvre.\nL’auteur est identifiée par son nom.")
    print("\nLe but c’est de vendre les audios aux clients identifiés par un numéro donnée en création du compte.\nChaque client a un nom, prénom et une date d’inscription.\nPour être client c’est pas nécessaire d’avoir acheté un œuvre.\n\n")
    


def print_description():
    print("--------Description-------------")
    print("\n----------Les clients------------------")
    print("\n(id, n, p, dn) ∈  LesClients ⇐⇒ le client identifie par le numero id, de nom n et de prenom p est inscrit dans la plateforme la date dn.")
    print("\n----------Les artistes------------------")
    print("\n(id, n) ∈  LesArtistes ⇐⇒ l’artiste identifie par le numero id est avec pseudonom n")
    print("\n----------Les types d'audios------------------")
    print("\n(t, l) ∈  LesTypes ⇐⇒ le type t est de longuer max l")
    print("\n----------Les oeuvres------------------")
    print("\n(id, n, p, t) ∈  LesOeuvres ⇐⇒ l’œuvre identifie par numéro id, de nom n est de prix p et aussi est de type t")
    print("\n----------Les oeuvres - clients------------------")
    print("\n(c, o) ∈  Œuvres_Clients ⇐⇒ l’œuvre identifie par numéro o, est acheté par le client c")
    print("\n----------Les oeuvres - artistes------------------")
    print("\n(a, o) ∈  Œuvres_Clients ⇐⇒ l’œuvre identifie par numéro o, est cree de taille ou entièrement par l’artiste a\n\n")


    
def print_help():
    print("--------Help-------------")
    print("les commandes possibles sont :")
    print("[-] description")
    print("[-] -d")
    print("[-] connect")
    print("[-] -c")
    print("[-] information")
    print("[-] -i")
    print("[-] quit")
    
def print_information():
    print("--------Information-------------")
    print("[-] clients")
    print("[-] auteurs")

# def print_connexion():
#     print("---------Connexion----------")
#     id = input("entrez votre id")
#     return id

def print_welcome_client():
    print("hello client")
def print_welcome_auteur():
    print("hello auteur")
