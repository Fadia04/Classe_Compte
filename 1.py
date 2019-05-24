class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir une classe Client avec les attributs suivants : CIN, Nom, Prénom, Tél.


# Attributs de la classe Client:
    CIN = "EE111222"
    nom = "SALIM"
    prenom = "Omar"
    tel = "06111111"

# On crée une instance de la classe Client:
client = Client() # client est un objet de type Client, c'est une instance de la classe Client

# Afficher les attributs de l'instance client:
print(client.CIN)
print(client.nom)
print(client.prenom)
print(client.tel)