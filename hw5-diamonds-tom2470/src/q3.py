import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def simple_train_test_split(X, y, test_size=.3):
    n_training_samples = int((1.0 - test_size) * X.shape[0])
    print(n_training_samples)
    X_train = X[:n_training_samples,:]
    y_train = y[:n_training_samples]

    X_test = X[n_training_samples:,:]
    y_test = y[n_training_samples:]

    return X_train, X_test, y_train, y_test
df=pd.read_csv('data/diamonds.csv')
df['logarithm_base2_price'] = np.log2(df['price'])
df['logarithm_base2_carat'] = np.log2(df['carat'])
model=LinearRegression()
X=df[['logarithm_base2_carat']]
X=X.to_numpy()
Y=df['logarithm_base2_price']
Y=Y.to_numpy()
X_train, X_test, y_train, y_test=simple_train_test_split(X,Y)
model.fit(X_train, y_train)
yhat = model.predict(X_test)
acc = explained_variance_score(y_test, yhat)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, Y, test_size=0.33, random_state=42)
model.fit(X_train2, y_train2)
yhat = model.predict(X_test2)
acc2 = explained_variance_score(y_test2, yhat)
print('the simple models explained varience is '+ str(acc)+'\nthe sklearn model explained varience is '+str(acc2))
figure, axis = plt.subplots(2, 2, sharex=True, sharey=True)
axis[0, 0].scatter(X_train, y_train, color='g', alpha=0.3)
axis[0, 0].set_title("simple train model")
axis[0, 1].scatter(X_test, y_test, color='g', alpha=0.3)
axis[0, 1].set_title("simple test model")
axis[1, 0].scatter(X_train2, y_train2, color='g', alpha=0.3)
axis[1, 0].set_title("Sklearn train model")
axis[1, 1].scatter(X_test2, y_test2, color='g', alpha=0.3)
axis[1, 1].set_title("Sklearn test model")
plt.savefig('figs/figure31.png')