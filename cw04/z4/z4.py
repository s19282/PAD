import numpy as np
import pandas as pd

m = np.genfromtxt('Zadanie_4.csv', delimiter=';', skip_header=False)
df = pd.read_csv('Zadanie_4.csv', delimiter=";")


df2 = df.groupby(['DateTime', 'DoctorID'])
print(df)
