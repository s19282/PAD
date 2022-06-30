import pandas as pd

df = pd.read_csv('csv/cars.csv')

print(df.shape)

df.drop_duplicates(inplace=True)

print(df.shape)

print(df.columns)

df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)

print(df.columns)

df.rename(columns={'seller type': 'seller'}, inplace=True)

print(df['seller'].unique())

df.seller = df.seller.str.replace('Osoby prywatnej', 'Private')
df.seller = df.seller.str.replace('Firmy', 'Dealer')

print(df['seller'].unique())

print(df['fuel'].unique())

df.fuel = df.fuel.str.replace('Benzyna', 'Petrol')
df.fuel = df.fuel.str.replace('Benzyna+LPG', 'Petrol+LPG', regex=False)
df.fuel = df.fuel.str.replace('Benzyna+CNG', 'Petrol+CNG', regex=False)
df.fuel = df.fuel.str.replace('Hybryda', 'Hybrid')
df.fuel = df.fuel.str.replace('Elektryczny', 'Electric')
df.fuel = df.fuel.str.replace('Wodór', 'Hydrogen')

print(df['fuel'].unique())

print(df['horse power'].unique())

df['horse power'] = df['horse power'].str.replace(' KM', '')

print(df['horse power'].unique())

print(df['capacity'].unique())

df.capacity = df.capacity.str.replace(' cm3', '').str.replace(' ', '')

print(df['capacity'].unique())

print(df['transmission'].unique())

df.transmission = df.transmission.str.replace('Automatyczna', 'Automatic')
df.transmission = df.transmission.str.replace('Manualna', 'Manual')

print(df['transmission'].unique())

print(df['drive train'].unique())

df['drive train'] = df['drive train'].str.replace('Na przednie koła', 'FWD')
df['drive train'] = df['drive train'].str.replace('Na tylne koła', 'RWD')
df['drive train'] = df['drive train'].str.replace('4x4 (dołączany automatycznie)', '4WD (automatic)', regex=False)
df['drive train'] = df['drive train'].str.replace('4x4 (stały)', '4WD (permanent)', regex=False)
df['drive train'] = df['drive train'].str.replace('4x4 (dołączany ręcznie)', '4WD (manual)', regex=False)

print(df['drive train'].unique())

print(df['body type'].unique())

df['body type'] = df['body type'].str.replace('Kombi', 'station wagon')
df['body type'] = df['body type'].str.replace('Kompakt', 'Compact')
df['body type'] = df['body type'].str.replace('Auta miejskie', 'City cars')
df['body type'] = df['body type'].str.replace('Auta małe', 'Small cars')
df['body type'] = df['body type'].str.replace('Kabriolet', 'Cabriolet')

print(df['body type'].unique())

print(df['doors'].unique())

print(df['seats'].unique())

print(df['color'].unique())

df['color'] = df['color'].str.replace('Inny kolor', 'Other')
df['color'] = df['color'].str.replace('Brązowy', 'Brown')
df['color'] = df['color'].str.replace('Niebieski', 'Blue')
df['color'] = df['color'].str.replace('Czarny', 'Black')
df['color'] = df['color'].str.replace('Srebrny', 'Silver')
df['color'] = df['color'].str.replace('Biały', 'White')
df['color'] = df['color'].str.replace('Beżowy', 'Beige')
df['color'] = df['color'].str.replace('Bordowy', 'Claret')
df['color'] = df['color'].str.replace('Szary', 'Gray')
df['color'] = df['color'].str.replace('Żółty', 'Yellow')
df['color'] = df['color'].str.replace('Czerwony', 'Red')
df['color'] = df['color'].str.replace('Zielony', 'Green')
df['color'] = df['color'].str.replace('Złoty', 'Gold')
df['color'] = df['color'].str.replace('Fioletowy', 'Violet')

print(df['color'].unique())

print(df['state'].unique())

df['state'] = df['state'].str.replace('Używane', 'Used')
df['state'] = df['state'].str.replace('Nowe', 'New')

print(df['state'].unique())

print(df['price'].unique())

df['price'] = df['price'].str.replace('EUR', '')\
                            .str.replace('        PLN', '', regex=False)\
                            .str.replace(' ', '')

print(df['price'].unique())

print(df['currency'].unique())

print(df['priceDetails'].unique())

df['priceDetails'] = df['priceDetails'].str.replace('Do negocjacji', 'Negotiable', regex=True)
df['priceDetails'] = df['priceDetails'].str.replace('Faktura VAT', 'VAT', regex=True)
df['priceDetails'] = df['priceDetails'].str.replace('Możliwość odliczenia VAT', 'VAT deduct', regex=True)

print(df['priceDetails'].unique())

print(df['serviced at aso'].unique())

df['serviced at aso'].fillna('False', inplace=True)
df['serviced at aso'] = df['serviced at aso'].str.replace('Tak', 'True')

print(df['serviced at aso'].unique())

print(df['first owner'].unique())

df['first owner'].fillna('False', inplace=True)
df['first owner'] = df['first owner'].str.replace('Tak', 'True')

print(df['first owner'].unique())

print(df['first owner'].unique())

df['damaged'].fillna('False', inplace=True)
df['damaged'] = df['damaged'].str.replace('Tak', 'True')

df.drop(['description', 'location', 'version', 'currency', 'priceDetails'], axis=1, inplace=True)
df.rename(columns={'horse power': 'horsePower'}, inplace=True)
df.rename(columns={'drive train': 'driveTrain'}, inplace=True)
df.rename(columns={'body type': 'bodyType'}, inplace=True)
df.rename(columns={'serviced at aso': 'ASOServiced'}, inplace=True)
df.rename(columns={'first owner': 'firstOwner'}, inplace=True)

print(df.columns)

df.to_csv('carsPrepared.csv', index=False)
