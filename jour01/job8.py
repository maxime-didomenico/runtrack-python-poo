class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return(self.rayon * self.rayon * 3.14)
    
    def diametre(self):
        return(self.rayon * 2)
    
    def changerRayon(self, value):
        self.rayon = value

    def afficherInfos(self):
        print("Rayon : " + str(self.rayon))
        print("Aire : " + str(self.aire()))
        print("Diametre : " + str(self.diametre()))

print("Cercle de rayon 21")

Cercle1 = Cercle(21)
Cercle1.afficherInfos()

print("\nCercle de rayon 42")

Cercle1.changerRayon(42)
Cercle1.afficherInfos()