import pandas as pd

customers = pd.read_csv('customers.csv', delimiter=",")
orders = pd.read_csv('orders.csv', delimiter=",")

print(orders.describe())
print(orders.info())
print(orders.head())
# a
orders['order_date'] = pd.to_datetime(orders['order_date'], format='%Y/%m/%d')
# b
print(orders['tshirt_category'].unique())
print(orders['tshirt_category'].unique().size)
# c
orders['tshirt_category'].replace(['Wh'], 'White', inplace=True)
orders['tshirt_category'].replace(['Bl'], 'Black', inplace=True)
orders['tshirt_category'].str.split().apply(lambda x: 'White' if x == 'Wh' else 'Black' if x == 'Bl' else x)

print(orders['tshirt_category'].unique())

#e
print(orders[orders.order_date.between('2014-12-31','2016-08-02')])