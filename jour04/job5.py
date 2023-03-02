class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):

    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius * self.radius


# Rectangle
 
rectangle = Rectangle(5, 10)
print("aire rectangle = ", rectangle.aire())

# Cercle

cercle = Cercle(5)
print("aire cercle = ", cercle.aire())