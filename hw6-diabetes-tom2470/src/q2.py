from sklearn import datasets
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.feature_selection import SequentialFeatureSelector as SFS
import matplotlib.pyplot as plt
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


mylist=[]
for i in range(1,10):
  selector = SFS(model,n_features_to_select=i,scoring='r2')
  selector.fit(data, y)
  f=list(selector.get_feature_names_out())
  for j in f:
    if j in mylist:
      continue
    mylist.append(j)
for i in r2scores.keys():
    if i in mylist:
      continue
    mylist.append(i)

myvalues=[]
for i in mylist:
  myvalues.append(r2scores[i])

plt.bar(mylist, myvalues, color='g')
plt.savefig('img/fig2.png')