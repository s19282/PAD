from z1.cat import Cat
from z1.dog import Dog
from z2.worker import Worker

dogM = Dog("Male")
dogF = Dog()

catM = Cat("Male")
catF = Cat()

newDog = dogF.breed(dogM)
print(newDog)

newCat = catF.breed(catM)
print(newCat)

# newNothing = catF.breed(dogM)

myList = [
    Worker(1, "Adam", 1983, 1500),
    Worker(2, "Anna", 1981, 1700),
    Worker(3, "Błażej", 1990, 1800),
    Worker(4, "Beata", 1992, 1600),
    Worker(5, "Czesław", 1980, 2000),
    Worker(6, "Cecylia", 1983, 2100),
    Worker(7, "Daniel", 1976, 1900)
]


def avgSal(workers):
    sal = 0
    companySize = 0

    for w in workers:
        sal += w.salary
        companySize += 1

    print(f'----------------\nAVG sal: {sal / companySize}\n----------------')


def avgSalWithAge(workers, age):
    salYounger = 0
    counterYounger = 0
    salOlder = 0
    counterOlder = 0

    for w in workers:
        if w.age[0] < age:
            salYounger += w.salary
            counterYounger += 1
        else:
            salOlder += w.salary
            counterOlder += 1
    print(f'----------------\nWorkers younger than {age} years old AVG salary: { 0 if salYounger==0 or counterYounger==0 else salYounger / counterYounger} '
          f'\nWorkers older (or equal) than {age} years old AVG salary: {0 if salOlder==0 or counterOlder==0 else salOlder / counterOlder}\n----------------')


avgSal(myList)
avgSalWithAge(myList, 30)
