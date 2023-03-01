class Tache:

    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTache:

    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def afficherListe(self):
        buff = []
        for tache in self.taches:
            buff.append(tache.titre)
        return buff
    
    def supprimerTache(self, tache):
        self.taches.remove(tache)
        print("\nTâche supprimée : " + tache.titre)

    def termineTache(self, tache):
        tache.statut = "Terminée"
        print("\nTâche terminée : " + tache.titre)
    
    def filtrerTache(self, statut):
        buff = []
        for tache in self.taches:
            if tache.statut == statut:
                buff.append(tache.titre)
        return buff
            
tache1 = Tache("Faire les courses", "Acheter du pain, du lait, des oeufs", "à faire")
tache2 = Tache("Faire la vaisselle", "Laver les assiettes, les verres, les couverts", "à faire")
tache3 = Tache("Faire le ménage", "Passer l'aspirateur, balayer, laver les sols", "à faire")
tache4 = Tache("Faire la lessive", "Laver les vêtements", "à faire")

liste = ListeDeTache()

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)

print("Tâches :")
for tache in liste.taches:
    print(tache.titre)

liste.supprimerTache(tache1)
liste.afficherListe()
liste.termineTache(tache2)

print("\nTâches :")
for tache in liste.taches:
    print(tache.titre)

print("\nTâches en cours :")
for tache in liste.filtrerTache("à faire"):
    print(tache)

print("\nTâches en terminées :")
for tache in liste.filtrerTache("Terminée"):
    print(tache)