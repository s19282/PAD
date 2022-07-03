import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


def plotPredictions(y_pred, y_test):
    samples = len(y_pred)
    plt.figure()
    plt.scatter(np.arange(samples), y_pred, c='r', label='predictions')
    plt.scatter(np.arange(samples), y_test, c='c', label='actual values', marker='x')
    plt.legend()
    plt.xlabel('Sample numbers')
    plt.ylabel('Values')
    plt.show()


def prepareSets(x, y):
    for col in x.columns:
        if x[col].dtypes == 'object':
            x[col] = le.fit_transform(x[col])

    return train_test_split(x, y, test_size=0.2, random_state=42)


def minimize_loss(x_train, y_train):
    X_with_bias = np.hstack((np.ones((x_train.shape[0], 1)), x_train))
    optimal_w = np.matmul(
        np.linalg.inv(np.array(np.matmul(X_with_bias.T, X_with_bias), dtype='float64')),
        np.matmul(X_with_bias.T, y_train),
    )
    return optimal_w[1:], optimal_w[0]


def fitModel(model, x_train, x_test, y_train, y_test):
    # weights, bias = minimize_loss(x_train=x_train, y_train=y_train)
    # model.set_params(weights, bias)
    model.fit(x_train, y_train)
    Y_pred = model.predict(x_test)

    print('RMSE: %.3f' % np.sqrt(mean_squared_error(y_test.values, Y_pred)))
    print('MAE: %.3f' % mean_absolute_error(y_test.values, Y_pred))
    print('R^2: %.3f' % r2_score(y_test.values, Y_pred))
    # plotPredictions(y_pred=Y_pred, y_test=y_test.values)

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
