from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
base_estimator = DecisionTreeClassifier(max_depth=1)
n_estimators = [10, 20, 30,40,50,60,70,80,90,100,200,500,1000]
train_scores = []
test_scores = []
for n in n_estimators:
    ada = AdaBoostClassifier(base_estimator=base_estimator, n_estimators=n)
    ada.fit(X_train, y_train)
    
    y_train_pred = ada.predict(X_train)
    y_test_pred = ada.predict(X_test)
    
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    
    train_scores.append(train_acc)
    test_scores.append(test_acc)

plt.figure(figsize=(10, 6))
plt.title("AdaBoost Classifier Performance")
plt.xlabel("Number of Estimators")
plt.ylabel("Accuracy")
plt.grid()

plt.plot(n_estimators, train_scores, label="Training Accuracy", marker="o")
plt.plot(n_estimators, test_scores, label="Test Accuracy", marker="s")

plt.legend()
plt.savefig('img/fig4.png')