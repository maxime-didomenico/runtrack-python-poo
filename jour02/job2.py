class Livre:

    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def set_titre(self, value):
        self.__titre = value

    def set_auteur(self, value):
        self.__auteur = value

    def set_nb_pages(self, value):
        if value > 0:
            self.__nb_pages = value
        else:
            print("Le nombre de pages doit être supérieur à 0")

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
book = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)

print("Titre =", book.get_titre(), "\nAuteur =", book.get_auteur(), "\nPages =", book.get_nb_pages(), "\n")

book.set_nb_pages(-1)
book.set_auteur("Stephen King")
book.set_titre("Shining")
book.set_nb_pages(500)

print("\nTitre =", book.get_titre(), "\nAuteur =", book.get_auteur(), "\nPages =", book.get_nb_pages())