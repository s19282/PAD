import pandas as pd

df1 = pd.read_csv('offers_0.csv')
df2 = pd.read_csv('offers_1.csv')
df3 = pd.read_csv('offers_2.csv')

print(df1.shape)
print(df2.shape)
print(df3.shape)

frames = [df1, df2, df3]

df4 = pd.concat(frames)

print(df4.shape)

df4.to_csv('cars.csv')
