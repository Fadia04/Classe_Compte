class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir un constructeur permettant d’initialiser le CIN, le nom et le prénom.

    def __init__(self): # la méthode constructeur.
        # On décrit les attributs:
        self.CIN = "EE111222"
        self.nom = "SALIM"
        self.prenom = "Omar"
       

client = Client()
client.CIN