
class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir une classe Client avec les attributs suivants : CIN, Nom, Prénom, Tél.

# Attributs de la classe Client:
    cin = "EE111222"
    nom = "SALIM"
    prenom = "Omar"
    tel = "06111111"

# Définir un constructeur permettant d’initialiser tous les attributs.
    def __init__(self, cin, nom, prenom, tel):
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
        self.tel = tel

# Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.
    def get_cin(self):
        return self.cin 
    def get_nom(self):
        return self.nom 
    def get_prenom(self):
        return self.prenom
    def get_tel(self):
        return self.tel

# Définir la méthode Afficher ( ) permettant d’afficher les informations du Client en cours.
    def afficher_client1(self):
        self.afficher_client1 = "- cin : " + str(self.cin), "nom : " + str(self.nom), "prenom : " + str(self.prenom), "tel : " + str(self.tel)
    
client1 = Client("EE111222", "SALIM", "Omar", "06111111")
print(client1.get_cin())
print(client1.get_nom())
print(client1.get_prenom())
print(client1.get_tel())

client1.afficher_client1()
print(client1.afficher_client1)


