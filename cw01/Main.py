from cat import Cat
from dog import Dog

dogM = Dog("Male")
dogF = Dog()

catM = Cat("Male")
catF = Cat()

newDog = dogF.breed(dogM)
print(newDog)

newCat = catF.breed(catM)
print(newCat)

newNothing = catF.breed(dogM)

