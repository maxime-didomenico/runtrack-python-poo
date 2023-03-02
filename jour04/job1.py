class Personne:

    def __init__(self, age):
        self.age = age
    
    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello !")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):

    def __init__(self, age):
        Personne.__init__(self, age)

    def allerEnCour(self):
        print("Je vais en cours.")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):

    def __init__(self, age):
        Personne.__init__(self, age)
        self.__matiereEnseignee = None

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee
    
    def setMatiereEnseignee(self, matiere):
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print(f"Le cours de {self.__matiereEnseignee} va commencer.")


# Eleve

eleve = Eleve(15)
eleve.afficherAge()
eleve.modifierAge(16)
eleve.afficherAge()
eleve.allerEnCour()


# Professeur

professeur = Professeur(30)
professeur.setMatiereEnseignee("Maths")
professeur.enseigner()