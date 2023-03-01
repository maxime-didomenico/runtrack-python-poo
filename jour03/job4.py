class Joueur:

    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        if self.cartons_jaunes == 1:
            self.recevoirUnCartonRouge()
            self.cartons_jaunes += 1
        if self.cartons_jaunes >= 2:
            pass
        else:
            self.cartons_jaunes += 1


    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} ({self.position}, numéro {self.numero}):")
        print(f"\tButs marqués : {self.buts_marques}")
        print(f"\tPasses décisives effectuées : {self.passes_decisives}")
        print(f"\tCartons jaunes reçus : {self.cartons_jaunes}")
        print(f"\tCartons rouges reçus : {self.cartons_rouges}")


class Equipe:
    
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques du club {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "buts":
                    joueur.marquerUnBut()
                elif action == "passes":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Messi", 10, "attaquant")
joueur2 = Joueur("Ronaldo", 7, "attaquant")
joueur3 = Joueur("Suarez", 9, "attaquant")
joueur4 = Joueur("Bale", 11, "attaquant")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques des joueurs

print("Equipe 1:")
equipe1.afficherStatistiquesJoueurs()

print("\nEquipe 2:")

equipe2.afficherStatistiquesJoueurs()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur("Messi", "buts")
equipe1.mettreAJourStatistiquesJoueur("Messi", "buts")
equipe1.mettreAJourStatistiquesJoueur("Messi", "buts")
equipe1.mettreAJourStatistiquesJoueur("Messi", "passes")
equipe1.mettreAJourStatistiquesJoueur("Messi", "passes")

equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "jaune")
print(' ')
equipe1.afficherStatistiquesJoueurs()
print(' ')
equipe2.afficherStatistiquesJoueurs()