import pandas as pd
import scipy as sp
import plotly.express as px
import statsmodels as sm

df = pd.read_csv('PAD_09_PD.csv', delimiter=";")
income_df = df.iloc[:, [0, 2]]

model = sm.ols
