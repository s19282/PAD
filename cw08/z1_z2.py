import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('PAD_09_PD.csv', delimiter=";")
income_df = df.iloc[:, [0, 2]]

model = smf.ols(formula='Annual_Income ~ Gender', data=income_df).fit()
print(model.summary())
# pvalues = model.pvalues
# max_p = pvalues.idxmax()
# alpha = 0.05
# while pvalues
