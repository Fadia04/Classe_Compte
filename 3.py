
class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
#  Définir un constructeur permettant d’initialiser tous les attributs.

    def __init__(self, client_attributes): # dico passé en paramètre.
        # on crée une boucle pour automatiser l'accès aux différents attributs.
        for attribute_name, attribute_value in client_attributes.items():
            setattr(self, attribute_name, attribute_value)

client_attributes = {"CIN" : "EE111222", "Nom" : "SALIM", "Prenom" : "Omar", "Tel" : "06111111"} # dictionnaire contenant les attributs et leurs valeurs


client = Client(client_attributes)
print(client.CIN) # On peut remplacer CIN par chacun des autres attributs.