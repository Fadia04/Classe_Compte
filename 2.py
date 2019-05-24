class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.

    def num_CIN(self, CIN):
        return "Le CIN est " + CIN

    def le_nom(self, nom):
        return "Le nom est " + nom

    def le_prenom(self, prenom):
        return "Le prénom est " + prenom

    def le_num_de_tel(self, tel):
        return "Le num de tel est " + tel

client = Client()
print(client.num_CIN("EE111222"))
print(client.le_nom("SALIM"))
print(client.le_prenom("Omar"))
print(client.le_num_de_tel("06111111"))

