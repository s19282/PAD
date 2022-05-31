import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import ttest_ind
import plotly.graph_objects as go

# z1

df = pd.read_csv('PAD_09_PD.csv', delimiter=";")
income_df = df.iloc[:, [0, 2]]
male = income_df.query('Gender == "Male"')['Annual_Income']
female = income_df.query('Gender == "Female"')['Annual_Income']
res = ttest_ind(male, female)
# p value > 0,05 nie możemy odrzucić hipotezy zerowej
print(res)

# 2

model = smf.ols(formula='Spending_Score ~ Gender + Age + Annual_Income', data=df).fit()
print(model.summary())
fig = go.Figure()
model2 = smf.ols(formula='Spending_Score ~ + Age + Annual_Income', data=df).fit()
print(model2.summary())
