from animal import Animal


class Dog(Animal):

    def __init__(self, gender="Female"):
        super().__init__("Canis", gender)

    def woof(self):
        """woof woof"""
