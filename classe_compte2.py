
class Compte: # définition de la classe Compte.
# classe définissant un compte caractérisé par:
# son solde
# un code qui est incrémenté lors de sa création
# son propriétaire qui représente un client
    solde = 0
    code  = 0
    proprietaire = "client"

    def __init__(self, solde, code, proprietaire):
        self.solde = solde
        self.code = code 
        self.proprietaire = proprietaire 

# Définir à l’aide des propriétés les méthodes d’accès aux différents
# attributs de la classe (le numéro de compte et le solde sont en lecture seule)
    def get_solde(self):
        return self.solde
    def get_code(self):
        return self.code 
    def get_proprietaire(self):
        return self.proprietaire

# Définir un constructeur permettant de créer un compte en indiquant son propriétaire.
    def __init__(self, code, solde, cin, nom, prenom, tel):
        self.solde = solde
        self.code = code 
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
        self.tel = tel

# Une méthode permettant de Crediter() le compte, prenant une somme en paramètre.
    def crediter(self, somme):
        self.solde = self.solde + somme
        return self.solde 

# Une méthode permettant de Crediter() le compte, prenant une somme et un compte en paramètres, créditant le compte et débitant le compte passé en paramètres.     
    def crediter1(self, somme, compte2):
        self.solde = self.solde + compte2
        return self.solde

# Une méthode permettant de Debiter() le compte, prenant une somme en paramètre    
    def debiter(self, somme):
        self.solde = self.solde - somme
        return self.solde 

# Une méthode permettant de Débiter() le compte, prenant une somme et un compte bancaire en paramètres, débitant le compte et créditant le compte passé en paramètres
    def debiter1(self, somme, compte2):
        self.solde = self.solde - compte2
        self.compte2 = compte2 + self.solde
        return self.compte2

# Une méthode qui permet d’afficher le résumé d’un compte.    
    def afficher_compte1(self):
        self.afficher_compte1 = "- code : " + str(self.code), "- solde: " +str(self.solde), "cin : " +str(self.cin), "nom : " + str(self.nom), "prenom : " + str(self.prenom), "tel : " +str(self.tel)
    def afficher_compte2(self):
        self.afficher_compte2 = "- code : " + str(self.code), "- solde: " +str(self.solde), "cin : " +str(self.cin), "nom : " + str(self.nom), "prenom : " + str(self.prenom), "tel : " +str(self.tel)  

                 
compte1 = Compte(0, 0, "EE111222", "SALIM", "Omar", "06111111")
compte2 = Compte(0, 0, "EE333444", "Karimi", "Samir", "06222222")
print(compte1.get_solde())
print(compte1.get_code())
print(compte2.get_solde())

compte1.crediter(5000)
print(compte1.solde)

compte1.crediter1(compte2, 2000)
print(compte1.solde)
compte2.debiter(2000)
print(compte2.solde)

compte1.debiter(1000)
print(compte1.solde)

compte1.debiter1(compte2, 1000)
print(compte1.solde)
compte2.crediter(1000)
print(compte2.solde)

compte1.afficher_compte1()
print(compte1.afficher_compte1) 
compte2.afficher_compte2()
print(compte2.afficher_compte2)


