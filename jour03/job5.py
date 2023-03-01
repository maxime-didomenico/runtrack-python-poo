import random

class Personnage:
    def __init__(self, nom, vie):

        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):

        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")
        adversaire.vie -= degats


class Jeu:

    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        niveaux = ["facile", "moyen", "difficile"]
        while True:
            choix = input(f"Choisissez le niveau de difficulté ({', '.join(niveaux)}) : \n")
            if choix.lower() in niveaux:
                self.niveau = choix.lower()
                break
            else:
                print("Niveau invalide.")

    def lancerJeu(self):
        
        self.choisirNiveau()

        if self.niveau == "facile":
            joueur1 = Personnage("joueur1", 100)
            joueur2 = Personnage("joueur2", 50)

        elif self.niveau == "moyen":
            joueur1 = Personnage("joueur1", 75)
            joueur2 = Personnage("joueur2", 75)

        else:
            joueur1 = Personnage("joueur1", 50)
            joueur2 = Personnage("joueur2", 100)

        print(f"{joueur1.nom} ({joueur1.vie} PV) VS {joueur2.nom} ({joueur2.vie} PV).\n")

        while joueur1.vie > 0 and joueur2.vie > 0:
            joueur1.attaquer(joueur2)
            joueur2.attaquer(joueur1)

            print(f"\n{joueur1.nom} a {joueur1.vie} PV.")
            print(f"{joueur2.nom} a {joueur2.vie} PV.\n")

        if joueur1.vie > 0:
            print(f"{joueur1.nom} WIN !")
        else:
            print(f"{joueur2.nom} WIN !")


jeu = Jeu()
jeu.lancerJeu()