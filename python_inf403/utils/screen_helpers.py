from utils.automate import *


def print_introduction():
    print("--------Introduction-------------")
    print("\nSonny a constitué une base de données relationnelle sur la plateforme de vente d’audio en ligne.\nSonny représente pour chaque audio identifie par une numéro, le nom et le prix de cette audio.\nChaque audio a un type spécifique, qui peut être podcast, livre audio ou autre en forme de string.\nAvec le type est associe une longueur max qui montre le longueur max que peut avoir l’audio.")
    print("\nLes audios sont créé entièrement ou partiellement(features) par des auteurs.\nPour être un auteur il faut nécessairement avoir crée ou moins une œuvre.\nL’auteur est identifiée par son nom.")
    print("\nLe but c’est de vendre les audios aux clients identifiés par un numéro donnée en création du compte.\nChaque client a un nom, prénom et une date d’inscription.\nPour être client c’est pas nécessaire d’avoir acheté un œuvre.\n\n")
    


def print_description():
    print("--------Description-------------")
    """
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
    """
    print("\nBienvenue dans le site de vente d'audio.")
    print("\nvous pouvez regarder les bases de donnees en tapant la commande information ou -i.")
    print("\nensuite vous pouvez consulter les differentes bases en tapant leurs nom :")
    print("[-] clients")
    print("[-] auteurs")
    print("[-] types")
    print("[-] oeuvres\n")
    print("Vous pouvez aussi vous connectez pour faire d'autre action.\n")
    print("\nDans le cas où vous etes connectez en tant que clients.\n")
    print("Pour consultez le catalogue vous pouvez tapez la commande catalogue.")
    print("puis tapez le type d'oeuvre que vous recherchez :")
    print("[-] song")
    print("[-] audiobook")
    print("[-] oeuvres\n")
    print("Pour acheter des oeuvre avec la commande buy suivie de l'id du produit.")
    print("Ex : buy 502\n")
    print("Vous pouvez aussi consultez votre historique d'achat avec la commande history ou -hist.\n")
    print("\nDans le cas où vous etes connectez en tant qu'auteur.")
    print("Pour consultez vos oeuvres vous pouvez tapez la commande history ou -hist\n")
    print("Vous pouvez aussi consultez vos statistique en tapant stat.")
    print("cette commande vous affichera la somme d'argent que vous avez faite en fonction du type d'audio\n")
    print("vous pouvez aussi ajouter une oeuvre en tapant la commande sell : ")
    print("il faudra ensuite donnes les information demandees :")
    print("[-] id")
    print("[-] prix")
    print("[-] type\n")
    print("\n\nvous pouvez retournez au menu a tout moment en tapant la commande main.")
    print("\n\nvous pouvez aussi quittez le programme à tout moment avec la commande quit.")
    print("********************************\n")
    

    
def print_help():
    print("--------Help-------------")
    print("les commandes possibles sont :")
    print("[-] description")
    print("[-] -d")
    print("[-] connect")
    print("[-] -c")
    print("[-] information")
    print("[-] -i")
    print("[-] main")
    print("[-] quit")

def print_help_auteur():
    print("--------Help Auteur-------------")
    print("les commandes possibles sont :")
    print("[-] history")
    print("[-] -hist")
    print("[-] sell")
    print("[-] -s")
    print("[-] main")
    print("[-] quit")

def print_help_client():
    print("--------Help Client-------------")
    print("les commandes possibles sont :")
    print("[-] history")
    print("[-] -hist")
    print("[-] buy")
    print("[-] -b")
    print("[-] main")
    print("[-] quit")

    
def print_information():
    print("--------Information-------------")
    print("[-] clients")
    print("[-] auteurs")
    print("[-] types")
    print("[-] oeuvres")

# def print_connexion():
#     print("---------Connexion----------")
#     id = input("entrez votre id")
#     return id

def print_welcome_client(param):
    print("\nBonjour client " + param["username"])
    print("\nid : " + str(param["id"]))
    print("\n")

def print_welcome_auteur(param):
    print("\nBonjour auteur " + param["username"])
    print("id : " + str(param["id"]))
    print("\n")

def input_oeuvre():
    id = input("Enter your creations id: ")
    name = input("Enter your creations name : ")
    name = "'" + name + "'"
    type = input("Type : ")
    type = "'" + type + "'"
    prix = input("Price : ")
    obj = {
        "id" : id,
        "name" : name,
        "type" : type,
        "prix" : prix
    }
    return obj
