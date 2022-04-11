import numpy as np
import pandas as pd
from datetime import timedelta

df = pd.read_csv('Zadanie_4.csv', delimiter=";")
df = df.iloc[:, :-4]
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['DateTime'].dt.date)
df2 = pd.DataFrame(df.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).first())
df2 = df2.iloc[:, 1:]
df2['HowLong'] = df.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).count()['DateTime']
df2['HowLong'] = pd.to_timedelta(df2['HowLong'], unit='m')
df2['hour'] = df2['DateTime'] + df2['HowLong']
df2['hour'] = df2['hour'].dt.time
df2['DateTime'] = df2['DateTime'].astype(str) + ' - ' + df2['hour'].astype(str)
df2 = df2.iloc[:, :-2]
col = df2.pop('DateTime')
df2.insert(0, col.name, col)
df2.to_csv('out.csv', index=False)
print(df2)

