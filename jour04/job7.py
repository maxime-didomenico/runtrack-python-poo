import random

couleur = ["coeur", "carreau", "pique", "trefle"]

class Carte:

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def tirageCarte(self):
        self.valeur = random.randint(2, 11)
        self.couleur = random.randint(1, 4)

    def afficherCarte(self):
        print("Vous venez de tirer un(e) ", self.valeur, " de ", couleur[self.couleur - 1])


class Blackjack(Carte):

    def __init__(self, valeur, couleur):
        Carte.__init__(self, valeur, couleur)
        self.main = []
        self.croupier = []
        self.check = "tirer"

    def tirageCarte(self):
        Carte.tirageCarte(self)
        self.main.append(self.valeur)

    def tirageAs(self):
        Carte.tirageCarte(self)
        if self.valeur == 11:
            self.main.append(1)
        else:
            self.main.append(self.valeur)

    def afficherCarte(self):
        Carte.afficherCarte(self)

    def afficherMain(self):
        print("Votre main est composée de : ")
        i = 0
        while i < len(self.main): 
            print(self.main[i])
            i += 1

    def calculerMain(self):
        print("Votre main vaut ", sum(self.main))

    def verifierMain(self):
        if sum(self.main) == 21 and len(self.main) == 2:
            print("Blackjack !")
        elif sum(self.main) > 21:
            print("Bust !")
        else:
            print("Vous pouvez continuer à tirer des cartes.")

    def mainCroupier(self):
        Carte.tirageCarte(self)
        self.croupier.append(self.valeur)
        Carte.tirageCarte(self)
        self.croupier.append(self.valeur)

        print("La main du croupier est composée de : ")
        i = 0
        while i < len(self.croupier):
            print(self.croupier[i])
            i += 1
        print("Le total de sa main s'élève à ", sum(self.croupier), "\n")
    
    def tirageCroupier(self):
        Carte.tirageCarte(self)
        if self.valeur == 11 and sum(self.croupier) + 1 <= 21:
            self.croupier.append(1)
        else:
            self.croupier.append(self.valeur)

        print("La main du croupier est désormais composée de : ")
        i = 0
        while i < len(self.croupier):
            print(self.croupier[i])
            i += 1
        print("Le total de sa main s'élève à ", sum(self.croupier), "\n")


    def jouer(self):

        i = 0

        print(f"--------------- Tour numero : {i} -------------------\n")

        self.mainCroupier()

        self.tirageCarte()
        self.afficherCarte()
        self.tirageCarte()
        self.afficherCarte()
        self.afficherMain()
        self.calculerMain()
        self.verifierMain()

        i+=1

        while sum(self.main) < 21:

            print(f"\n--------------- Tour numero : {i} -------------------\n")

            self.check = input("\nVoulez vous tirer ou rester\n")

            if self.check == "tirer":
                self.tirageAs()
                self.afficherCarte()
                self.afficherMain()
                self.calculerMain()
                self.verifierMain()

                if sum(self.main) > 21:
                    break

            elif self.check == "rester":
                print("Vous avez choisi de rester.\n")
                
                while sum(self.croupier) < 17:
                    self.tirageCroupier()
                    if sum(self.croupier) > 21:
                        print("Le croupier a bust !")
                        exit()
                    elif sum(self.croupier) == 21:
                        print("Le croupier a fait un blackjack !")
                        exit()

                if sum(self.croupier) > sum(self.main):
                    print("Le croupier a gagné !")
                    exit()

                elif sum(self.croupier) < sum(self.main):
                    print("Vous avez gagné !")
                    exit()

                elif sum(self.croupier) == sum(self.main):
                    print("Egalité !")
                    exit()

            i+=1


blackjack = Blackjack(0, 0)
blackjack.jouer()