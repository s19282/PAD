import pandas as pd

# z1
print("-----z1------")
df = pd.read_csv('PAD_03_PD.csv', delimiter=";")
df.fillna(df.mode().iloc[0], inplace=True)
print(df['Country'].value_counts())
# z2
print("-----z2------")
df['owned_goods'] = df['owns_car']+df['owns_TV']+df['owns_house']+df['owns_Phone']
print(df)
# z3
print("-----z3------")
print(df.groupby(['gender']).mean().round(2))
# z4
print("-----z4------")
df2 = pd.DataFrame()
df2['owned_goods_avg'] = df.groupby(['Country']).mean().round(2)['owned_goods']
df2['min_age'] = df.groupby(['Country']).min('Age')['Age']
print(df2)