import pandas as pd
import statsmodels.formula.api as smf
import plotly.express as px

df = pd.read_csv('carsPrepared.csv')

model = smf.ols(formula='price ~ seller + make + model + year + capacity + fuel + horsePower + transmission '
                        '+ driveTrain + bodyType + doors + seats + color + state + ASOServiced + firstOwner + damaged',
                data=df).fit()
print(model.summary())

fig = px.imshow(df.corr())
fig.show()

yearPrice = pd.DataFrame()
yearPrice['year'] = df.year
yearPrice['price'] = df.price

yearAVGPrice = yearPrice.groupby(['year']).mean().reset_index()
fig = px.scatter(yearAVGPrice, "year", "price", title="Average price of vehicle grouped by year")
fig.show()

yearPrice = pd.DataFrame()
yearPrice['year'] = df.year
yearPrice['mileage'] = df.mileage

mileageAVGPrice = yearPrice.groupby(['year']).mean().reset_index()
fig = px.scatter(mileageAVGPrice, "year", "mileage", title="Average mileage of vehicle grouped by year")
fig.show()

fig = px.scatter(df.iloc[:, [14, 6]].groupby(['price']).mean().reset_index(), "price", "horsePower",
                 title="Average horse power of vehicle grouped by price")
fig.show()
