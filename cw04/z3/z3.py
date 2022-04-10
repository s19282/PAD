import numpy as np

a = np.genfromtxt('Zadanie_3_macierz_A.csv', delimiter=',', skip_header=False)
b = np.genfromtxt('Zadanie_3_macierz_B.csv', delimiter=',', skip_header=False)

c = np.matrix.sum(a * b)/np.sqrt(np.matrix.sum(a**2)*np.sqrt(np.matrix.sum(b**2)))
print(c)

