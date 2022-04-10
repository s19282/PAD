import numpy as np

m = np.genfromtxt('Zadanie_1.csv', delimiter=';', skip_header=True)
# a
print(m.size)
# b
print(m.shape)
# c
print(np.mean(m))
print(np.std(m))
print(np.median(m))
# d
print(np.nanmean(m))
print(np.nanstd(m))
print(np.nanmedian(m))
