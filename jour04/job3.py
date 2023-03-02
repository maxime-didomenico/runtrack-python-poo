class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = 0
        self.__largeur = 0

    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):

    def __init__(self, longeur, largeur, hauteur):
        Rectangle.__init__(self, longeur, largeur)
        self.__hauteur = 0
    
    def getHauteur(self):
        return self.__hauteur
    
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur


# Rectangle

rectangle = Rectangle(0, 0)

rectangle.setLongueur(20)
rectangle.setLargeur(40)

print("Rectangle :")
print("surface =", rectangle.surface())
print("perimetre =", rectangle.perimetre())

# Parallelepipede

parallelepipede = Parallelepipede(0, 0, 0)

parallelepipede.setLongueur(20)
parallelepipede.setLargeur(30)
parallelepipede.setHauteur(40)

print("\nParallelepipede :")
print("surface =", parallelepipede.surface())
print("volume =", parallelepipede.volume())