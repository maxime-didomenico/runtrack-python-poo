class Student:

    def __init__(self, firstname , name, age, id):
        self.__firstname = firstname
        self.__name = name
        self.__age = age
        self.__id = id
        self.__credit = 0
        self.__level = self.__StudentEval()

    def set_firstname(self, value):
        self.__firstname = value

    def set_name(self, value):
        self.__name = value

    def set_age(self, value):
        self.__age = value  

    def set_id(self, value):
        self.__id = value

    def set_credit(self, value):
        self.__credit = value

    def get_firstname(self):
        return self.__firstname

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_id(self):
        return self.__id
    
    def get_credit(self):
        return self.__credit
    
    def get_level(self):
        return self.__level
    
    def add_credit(self, value):
        if value > 0:
            self.__credit += value
            self.__level = self.__StudentEval()
        else:
            print("Le nombre de crédits doit être supérieur à 0")

    def __StudentEval(self):
        if self.__credit < 60:
            return "Insuffisant"
        if self.__credit >= 60 and self.__credit < 70:
            return "Passable"
        if self.__credit >= 70 and  self.__credit < 80:
            return "Bien"
        if self.__credit >= 80 and self.__credit < 90:
            return "Très bien"
        if self.__credit >= 90:
            return "Excellent"

student = Student("John", "Doe", 20, 145)

print("Le nombre de crédits de", student.get_firstname(), student.get_name(), " est de", student.get_credit(), "\n")

i = 0
while i < 3:
    print("Ajout de 30 crédits")
    student.add_credit(30)
    i += 1

print("\nLe nombre de crédits de", student.get_firstname(), student.get_name(), " est de", student.get_credit())
print("\nNom =", student.get_name(), "\nPrénom =", student.get_firstname(), "\nAge =", student.get_age(), "\nID =", student.get_id(), "\nNiveau =", student.get_level(), "\n")