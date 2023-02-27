class SePresenter():

    def __init__(self, firstname, name):
        self.prenom = firstname
        self.nom = name

    def sePresenter(self):
        return(self.prenom, self.nom)
    
First_Person = SePresenter("John", "Doe")
Second_Person = SePresenter("Jane", "Doe")

def print_name(firstname, name):
    print("Bonjour, je m'appelle ", firstname, " ", name)

name, firstname = First_Person.sePresenter()
print_name(firstname, name)
name, firstname = Second_Person.sePresenter()
print_name(firstname, name)