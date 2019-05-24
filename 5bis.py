class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir la méthode Afficher ( ) permettant d’afficher les informations du Client en cours.

    def afficher(self):
        self.CIN = "EE111222"
        self.Nom = "SALIM"
        self.Prenom = "Omar"
        self.Tel = "06111111"
        print(self.CIN, self.Nom, self.Prenom, self.Tel)


client = Client()
client.afficher()