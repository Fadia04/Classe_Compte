class Client: # définition de la classe Client.
# classe définissant un client caractérisé par:
# son CIN
# son nom
# son prénom
# son num de tel
# Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.
    CIN = "EE111222"
    nom = "SALIM"
    prenom = "Omar"
    tel = "06111111"

    def __init__(self):
        self._CIN = "EE111222"
        self._nom = "SALIM"
        self._prenom = "Omar"
        self._tel = "06111111"

    def _get_CIN(self):
        print("le CIN est")
        return self._CIN
    def _set_CIN(self, a):
        print("modification du CIN")
        self._CIN = a 

    def _get_nom(self):
        print("le nom est")
        return self._nom   
    def _get_prenom(self):
        print("le prenom est")
        return self._prenom 
    def _get_tel(self):
        print("le tel est")
        return self._tel 

    CIN = property(_get_CIN, _set_CIN)
    nom = property(_get_nom)
    prenom = property(_get_prenom)
    tel = property(_get_tel)
client = Client()