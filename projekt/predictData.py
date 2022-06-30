import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def prepareSets(x, y):
    # TODO: normalize data
    for col in x.columns:
        if x[col].dtypes == 'object':
            x[col] = le.fit_transform(x[col])

    return train_test_split(x, y, test_size=0.2, random_state=42)


def fitModel(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    Y_pred = model.predict(x_test)

    print('RMSE: %.3f' % np.sqrt(mean_squared_error(y_test.values, Y_pred)))
    print('MAE: %.3f' % mean_absolute_error(y_test.values, Y_pred))
    print('R^2: %.3f' % r2_score(y_test.values, Y_pred))

    print('----------------------------------------')


def evaluateModel(model, name):
    print("=====================")
    print(name)
    print("=====================")

    x = df.copy()
    y = df['price']

    x.drop(columns=['price'], inplace=True)

    X_train, X_test, Y_train, Y_test = prepareSets(x, y)
    fitModel(model, X_train, X_test, Y_train, Y_test)

    # removed bodyType, doors, seats, color, state, ASOServiced, firstOwner, damaged
    x.drop(columns=['bodyType', 'doors', 'seats', 'color', 'state', 'ASOServiced', 'firstOwner', 'damaged'],
           inplace=True)

    X_train, X_test, Y_train, Y_test = prepareSets(x, y)
    fitModel(model, X_train, X_test, Y_train, Y_test)

    # removed seller make model fuel transmission driveTrain
    x.drop(columns=['seller', 'make', 'model', 'fuel', 'transmission', 'driveTrain'], inplace=True)

    X_train, X_test, Y_train, Y_test = prepareSets(x, y)
    fitModel(model, X_train, X_test, Y_train, Y_test)


# start

df = pd.read_csv('carsPrepared.csv')
df.dropna(inplace=True)

le = preprocessing.LabelEncoder()

lr = LinearRegression()
evaluateModel(lr, "LinearRegression")

# lr2 = LogisticRegression(max_iter=1000)
# evaluateModel(lr2, "LogisticRegression")

dtr = DecisionTreeRegressor(max_depth=12)
evaluateModel(dtr, "DecisionTreeRegression")
