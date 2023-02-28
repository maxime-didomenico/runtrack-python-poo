class Voiture:

    def __init__(self, marque, modele, year, km):
        self.__marque = marque
        self.__modele = modele
        self.__year = year
        self.__km = km
        self.__reservoir = 50
        self.en_marche = False

    def set_marque(self, value):
        self.__marque = value

    def set_modele(self, value):
        self.__modele = value

    def set_year(self, value):
        self.__year = value

    def set_km(self, value):
        self.__km = value

    def set_reservoir(self, value):
        self.__reservoir = value

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_year(self):
        return self.__year
    
    def get_km(self):
        return self.__km
    
    def get_reservoir(self):
        return self.__reservoir
    
    def demarrer(self):
        if self.__verifier_plein() == True:
            self.en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est vide, la voiture ne peut pas démarrer.")
    
    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        if self.get_reservoir() <= 5:
            return False
        else:
            return True
        

Tesla = Voiture("Tesla", "Model S", 2019, 0)

Tesla.demarrer()
Tesla.arreter()

Tesla.set_reservoir(5)

Tesla.demarrer()

Tesla.arreter()