import random


class Animal:

    def __init__(self, genus, gender="Female"):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == "Female" and self.genus == partner.genus and partner.gender == "Male":
            return Animal(self.genus, "Male" if random.randint(1, 10) > 5 else "Female")
        else:
            raise Exception('Attribute not found!')

    def __str__(self):
        return f'----------------\nIs alive: {self.isAlive} ' \
               f'\nGender: {self.gender} \nGenus: {self.genus}\n----------------'
