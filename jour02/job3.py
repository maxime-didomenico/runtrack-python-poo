class Livre:

    def __init__(self, titre, auteur, nb_pages, disponibilité):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponibilité = True

    def set_titre(self, value):
        self.__titre = value

    def set_auteur(self, value):
        self.__auteur = value

    def set_nb_pages(self, value):
        if value > 0:
            self.__nb_pages = value
        else:
            print("Le nombre de pages doit être supérieur à 0")

    def set_disponibilité(self, value):
        self.__disponibilité = value

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def get_disponibilité(self):
        return self.__disponibilité
    
    def verification(self):
        if self.__disponibilité == True:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.verification() == True:
            self.__disponibilité = False
            return True
        else:
            return False
    
    def rendre(self):
        if self.verification() == False:
            self.__disponibilité = True
            return True
        else:
            return False
        
book = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96, True)

print("Titre =", book.get_titre(), "\nAuteur =", book.get_auteur(), "\nPages =", book.get_nb_pages(), "\nPages =", book.get_disponibilité(), "\n")

book.set_nb_pages(-1)

print("\nLe livre est emprunté.")

book.emprunter()

print("\nTitre =", book.get_titre(), "\nAuteur =", book.get_auteur(), "\nPages =", book.get_nb_pages(), "\nPages =", book.get_disponibilité(), "\n")

print("\nLe livre est rendu.")
book.rendre()

print("\nTitre =", book.get_titre(), "\nAuteur =", book.get_auteur(), "\nPages =", book.get_nb_pages(), "\nPages =", book.get_disponibilité(), "\n")