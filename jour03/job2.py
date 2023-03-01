class CompteBancaire:
     
    def __init__(self, num_compte, prenom, nom, solde, decouvert):
        self.__num_compte = num_compte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.decouvert = decouvert

    def get_num_compte(self):
        return self.__num_compte

    def get_prenom(self):
        return self.__prenom

    def get_nom(self):
        return self.__nom

    def get_solde(self):
        return self.__solde

    def set_solde(self, solde):
        self.__solde = solde

    def afficher(self):
        print("Les informations du compte bancaire sont :", "\n", self.__num_compte, "\n", self.__prenom, "\n", self.__nom, "\n", self.__solde)

    def afficherSolde(self):
        print("Le solde du compte bancaire de",self.__prenom, self.__nom, "est de :", self.__solde)

    def retrait(self, montant):
        self.__solde -= montant

    def virement(self, montant, compte):
        if compte.agios() == True:
            self.__solde -= montant
            compte.__solde += montant
        else:
            print("Le compte de", compte.__prenom, compte.__nom, "n'est pas autorisé à avoir un découvert")

    def agios(self):
        if self.__solde < 0 and self.decouvert == True:
            self.__solde -= 20
            return True
        else:
            return False
    
compte1 = CompteBancaire(123456789, "Jean", "Dupont", 1000, True)
compte1.afficher()
compte1.afficherSolde()

compte2 = CompteBancaire(987654321, "Marie", "Durand", -10, False)
compte2.afficher()
compte2.afficherSolde()

compte1.virement(100, compte2)
compte1.afficherSolde()
compte2.afficherSolde()