import random
from typing import Tuple


class Animal:

    def __init__(self, genus, gender="Female"):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender != "Female":
            print("NotFemale")
        elif partner.gender != "Male":
            print("PartnerNotMale")
        elif self.genus != partner.genus:
            print("Different genus")
        else:
            return Animal(self.genus, "Male" if random.randint(1, 10) > 5 else "Female")

    def __str__(self):
        return f'----------------\nIs alive: {self.isAlive} ' \
               f'\nGender: {self.gender} \nGenus: {self.genus}\n----------------'


