class Ville:

    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_nom(self):
        return self.__nom
    
    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

class Personne:

    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def set_ville(self, ville):
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.set_population(self.__ville.get_population() + 1)

ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

print("Population de la ville de Paris :", ville1.get_population(), "habitants.")
print("Population de la ville de Marseille :", ville2.get_population(), "habitants.")

jean = Personne("Jean", 25, ville1)
jean.ajouterPopulation()
myrtille = Personne("Myrtille", 4, ville1)
myrtille.ajouterPopulation()
chloe = Personne("Chloe", 18, ville2)
chloe.ajouterPopulation()

print("Mise à jour de la ville de Paris :", ville1.get_population(), "habitants.")
print("Mise à jour de la ville de Marseille :", ville2.get_population(), "habitants.")