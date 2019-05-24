class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Attributs de la classe Client:
    CIN = "EE111222"
    nom = "SALIM"
    prenom = "Omar"
    tel = "06111111"

    def __init__(self):
        self.CIN = "EE111222"
        self.nom = "SALIM"
        self.prenom = "Omar"
        self.tel = "06111111"
client = Client()     

# La classe Compte hérite de la classe Client: Elle récupère ses attributs et ses méthodes. 
class Compte(Client): # définition de la classe Compte.
# classe définissant un compte caractérisé par:
# son solde
# un code qui est incrémenté lors de sa création
# son propriétaire qui représente un client caractérisé par:
    # son CIN
    # son nom
    # son prénom
    # son tel
# Créer Une classe Compte caractérisée par son solde et un code qui est incrémenté lors de sa création ainsi que son propriétaire qui représente un client.
# Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe (le numéro de compte et le solde sont en lecture seule)
    solde = 0
    code = 0
    proprietaire = "client"
    def __init__(self):
        self.solde = 0
        self.code += 1
        self.proprietaire = "client"
    
compte = Compte()
