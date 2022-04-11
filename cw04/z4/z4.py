import numpy as np
import pandas as pd

df = pd.read_csv('Zadanie_4.csv', delimiter=";")
df = df.iloc[:, :-4]
df['DateTime'] = pd.to_datetime(df['DateTime'])
print(df.groupby([df['DateTime'].dt.day, 'DoctorID', 'Type', 'City']).head())
