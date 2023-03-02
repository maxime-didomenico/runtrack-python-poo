class Veicule():

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVeicule(self):
        print("Marque : ", self.marque)
        print("Modèle : ", self.modele)
        print("Année : ", self.annee)
        print("Prix : ", self.prix)

    def demarrer(self):
        print("Attention je roule.")


class Voiture(Veicule):

    def __init__(self, marque, modele, annee, prix):
        Veicule.__init__(self, marque, modele, annee, prix)
        self.porte = 4

    def informationVehicule(self):
        Veicule.informationVeicule(self)
        print("Porte : ", self.porte)

    def demarrer(self):
        print("Attention je roule en voiture.")


class Moto(Veicule):
    
        def __init__(self, marque, modele, annee, prix):
            Veicule.__init__(self, marque, modele, annee, prix)
            self.roue = 2
    
        def informationVehicule(self):
            Veicule.informationVeicule(self)
            print("Nombre de roue : ", self.roue)

        def demarrer(self):
            print("Attention je roule en moto.")


# Voiture

print("Voiture")
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationVehicule()
voiture.demarrer()


# Moto

print("\nMoto")
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationVehicule()
moto.demarrer()