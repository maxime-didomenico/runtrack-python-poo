class Produit:

    def __init__(self):
        self.nom = ""
        self.prixHT = 0
        self.TVA = 20

    def modifierNom(self, value):
        self.nom = value

    def modifierPrixHT(self, value):
        self.prixHT = value

    def CalculerPrixTTC(self):
        return(self.prixHT + (self.prixHT * self.TVA / 100))
    
    def return_nom(self):
        return self.nom
    
    def return_prixHT(self):
        return self.prixHT
    
    def return_TVA(self):
        return self.TVA
    
    def return_prixTTC(self):
        return self.CalculerPrixTTC()
    
    def listeProduit(self):
        return "Nom : " + self.nom + "\nPrixHT : " + str(self.prixHT) + "\nTVA : " + str(self.prixHT * self.TVA / 100) + "(" + str(self.TVA) + "%" + ")" + "\nPrixTTC : " + str(self.CalculerPrixTTC())

Produit1 = Produit()
Produit1.modifierNom("Iphone 14")
Produit1.modifierPrixHT(666)

print(Produit1.listeProduit())

print("\n")

Produit1.modifierNom("Playstation 5")
Produit1.modifierPrixHT(416)

print(Produit1.listeProduit())