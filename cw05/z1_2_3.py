import pandas as pd

customers = pd.read_csv('customers.csv', delimiter=",")
orders = pd.read_csv('orders.csv', delimiter=",")
# z1
print(orders.describe())
print(orders.info())
print(orders.head())
# a
orders['order_date'] = pd.to_datetime(orders['order_date'], format='%Y/%m/%d')
# b
print(orders['tshirt_category'].unique())
print(orders['tshirt_category'].unique().size)
# c
orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Wh ', 'White '))
orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Bl ', 'Black '))
orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Tshirt ', 'T-Shirt '))

print(orders['tshirt_category'].unique())


# d
def tshirt_type(type_):
    for el in type_:
        if el in ['T-Shirt', 'Hoodie', 'Tennis Shirt']:
            return el
    return 'No data'


def tshirt_size(size_):
    for el in size_:
        if el in ['M', 'F']:
            return el
    return 'No data'


def tshirt_colour(colour_):
    for el in colour_:
        if el in ['White', 'Black']:
            return el
    return 'No data'


orders['tshirt_type'] = orders['tshirt_category'].str.split().apply(lambda x: tshirt_type(x))
orders['tshirt_size'] = orders['tshirt_category'].str.split().apply(lambda x: tshirt_size(x))
orders['tshirt_colour'] = orders['tshirt_category'].str.split().apply(lambda x: tshirt_colour(x))
# e
print(orders[orders.order_date.between('2014-12-31', '2016-08-02')])

# z2

# a
print(customers.info())
# b
print("customers ", customers.shape, "orders ", orders.shape)
# c
customers.rename(columns={'customerID': 'customer_id'}, inplace=True)
# d
result = pd.merge(customers, orders, on='customer_id', how='inner')
# Wybrałem metodę merge i inner join co spowoduje zignorowanie zamówień bez klienta i klientów którzy nic nie zamówili
# z3
result.to_csv('out.csv', index=False)
