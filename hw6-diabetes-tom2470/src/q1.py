from sklearn import datasets
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
model=LinearRegression()
diabetes = datasets.load_diabetes(as_frame=True)
data=diabetes.data
target=diabetes.target
r2scores={}
for i in data.columns:
  X=np.array(data[i]).reshape(1, -1).transpose()
  y=np.array(target)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)
  model.fit(X_train, y_train)
  yhat = model.predict(X_test)
  acc = r2_score(y_test, yhat)
  r2scores[i]=acc
df=pd.DataFrame(r2scores, index=list(range(len(r2scores))))
import matplotlib.pyplot as plt
mylist = sorted(r2scores.items(), key=lambda x:x[1])
r2scores = dict(mylist)
plt.bar(r2scores.keys(), r2scores.values(), color='g')
plt.savefig('img/fig1.png')

model = LinearRegression()
diabetes = datasets.load_diabetes(as_frame=True)
data = diabetes.data
target = diabetes.target

squared_correlations = {}

for i in data.columns:
    X = np.array(data[i]).reshape(-1, 1)
    y = np.array(target)
    r2 = r2_score(y, X)
    squared_correlations[i] = r2

# Sort the squared correlations dictionary
sorted_correlations = dict(sorted(squared_correlations.items(), key=lambda x: x[1], reverse=True))

plt.bar(sorted_correlations.keys(), sorted_correlations.values(), color='g')
plt.savefig('img/fig1.png')