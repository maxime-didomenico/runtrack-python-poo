class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        return(self.x,self.y)

Personnage1 = Personnage()

print("Appel de la methode position() :", Personnage1.position(), "\n")

Personnage1.gauche()
Personnage1.bas()

print("Mouvement gauche et bas")
print("Appel de la methode position() :", Personnage1.position(), "\n")

Personnage1.droite()
Personnage1.haut()

print("Mouvement droite et haut")
print("Appel de la methode position() :", Personnage1.position())