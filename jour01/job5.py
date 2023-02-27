class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("coord (", str(self.x) + ", " + str(self.y), ")")

    def afficherX(self):
        print(str(self.x))
    
    def afficherY(self):
        print(str(self.y))

    def changerX(self, new_value):
        self.x = new_value

    def changerY(self, new_value):
        self.y = new_value

Point1 = Point(0,42)
Point1.afficherLesPoints()
Point1.changerX(21)
Point1.afficherLesPoints()