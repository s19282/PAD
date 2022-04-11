import numpy as np
import pandas as pd

df = pd.read_csv('Zadanie_4.csv', delimiter=";")
df = df.iloc[:, :-4]
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['DateTime'].dt.date)
print(df.groupby(['Date', 'DoctorID', 'Type', 'City']).first())
print(df.groupby(['Date', 'DoctorID', 'Type', 'City']).count())
# print(df.groupby(['Date', 'DoctorID', 'Type', 'City']).count().first())

# print(df.groupby([pd.Grouper(key='DateTime', freq='2D'), 'DoctorID', 'Type', 'City']).head())
