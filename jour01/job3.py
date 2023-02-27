class Operation_Job3:

    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 42

    def add(self):
        print(self.nombre1, " + ", self.nombre2, " = ", self.nombre1 + self.nombre2)

Operation2 = Operation_Job3()
Operation2.add()