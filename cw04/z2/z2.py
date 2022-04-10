import numpy as np

m = np.genfromtxt('Zadanie_2.csv', delimiter=';', skip_header=False)

# a
print(np.linalg.eig(m))
# b
print(np.linalg.inv(m))
