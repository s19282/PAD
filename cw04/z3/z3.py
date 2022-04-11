import numpy as np

a = np.genfromtxt('Zadanie_3_macierz_A.csv', delimiter=',', skip_header=False)
b = np.genfromtxt('Zadanie_3_macierz_B.csv', delimiter=',', skip_header=False)

c = np.dot(a, b.T)/(np.linalg.norm(a)*np.linalg.norm(b))
print(c)

