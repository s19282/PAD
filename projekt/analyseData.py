from statistics import mode
from matplotlib.pyplot import title
import pandas as pd
import statsmodels.formula.api as smf
import plotly.express as px
import plotly.graph_objects as go

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

yearAVGPrice = yearPrice.groupby(['year']).median().reset_index()
fig = go.Figure()
fig.add_trace(
        go.Scatter(x=yearAVGPrice["year"], y=yearAVGPrice["price"], mode="markers"))
fig.update_layout(title="Median price of vehicle grouped by year", xaxis_title="Year")
fig.show()

yearMileage = pd.DataFrame()
yearMileage['year'] = df.year
yearMileage['mileage'] = df.mileage

yearAVGMileage = yearMileage.groupby(['year']).median().reset_index()
fig = go.Figure()
fig.add_trace(
        go.Scatter(x=yearAVGMileage["year"], y=yearAVGMileage["mileage"], mode="markers"))
fig.update_layout(title="Median mileage of vehicle grouped by year", xaxis_title="Year")
fig.show()



# fig = px.scatter(df.iloc[:, [14, 6]].groupby(['price']).mean().reset_index(), "price", "horsePower",
#                  title="Average horse power of vehicle grouped by price")
# fig.show()
