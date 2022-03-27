l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x: x * x
cube = lambda x: x * x * x
[print(x, '\tsquare: ', square(x), ' cube: ', cube(x)) for x in l]
