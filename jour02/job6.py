class Commande:

    def __init__(self, numero):
        self.__numero = numero
        self.__plats = {}
        self.__statut = "En cours"

    def ajouter_plat(self, nom, prix):
        if nom not in self.__plats:
            self.__plats[nom] = {"prix": prix, "statut": self.__statut}
        else:
            print("Le plat est déjà dans la commande\n")

    def annuler_commande(self):
        self.__plats.clear()
        self.__statut = "Annulée"

    def terminer_commande(self):
        self.__statut = "Terminée"
        for plat in self.__plats.values():
            plat["statut"] = "Terminée"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats.values():
            if plat["statut"] == "Terminée" or plat["statut"] == "En cours":
                total += plat["prix"]
        return total

    def afficher_commande(self):
        print("Commande n°", self.__numero)
        print("Statut : ", self.__statut)
        for plat, infos in self.__plats.items():
            print("- ", plat, " : ", infos["prix"], "€ (", infos["statut"], ")")
        total = self.__calculer_total()
        print("Total : ", total, "€\n")

    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.2
        return tva

command1 = Commande(1)

command1.ajouter_plat("Pizza", 10)
command1.ajouter_plat("Coca", 5)
command1.ajouter_plat("Coca", 5)
command1.ajouter_plat("Coffee", 4)

command1.afficher_commande()
command1.terminer_commande()

command1.afficher_commande()
print("\n")
command1.annuler_commande()
command1.afficher_commande()