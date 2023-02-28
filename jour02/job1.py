class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def set_length(self, value):
        self.length = value

    def set_width(self, value):
        self.width = value

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width

object = Rectangle(10, 5)

print("Longueur =", object.get_length(), "\nLargeur =", object.get_width())

object.set_length(20)
object.set_width(10)

print("\nLongueur =", object.get_length(), "\nLargeur =", object.get_width())
