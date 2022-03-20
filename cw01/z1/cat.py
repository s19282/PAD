from z1.animal import Animal


class Cat(Animal):

    def __init__(self, gender="Female"):
        super().__init__("Felis", gender)

    def purr(self):
        """purr"""
