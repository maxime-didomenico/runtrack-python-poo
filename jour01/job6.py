class Animal:
    
    def __init__(self):
        self.age = 0
        self.name = ""
    
    def nommer(self, name):
        self.name = name
        print("Le nom de l'animal est " + self.name)
    
    def viellir(self):
        self.age += 1
        print(self.name, "est âgé de " + str(self.age) + "ans.")

Animal1 = Animal()
Animal1.nommer("Toto")

Animal1.viellir()
print("#age de l'animal après appel de la methode viellir()")
Animal1.viellir()