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
digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = GaussianNB()
model.fit(X_train, y_train)
y_model = model.predict(X_test)
param_range = np.arange(0, 100, 5)
train_scores, test_scores = validation_curve( RandomForestClassifier(), X, y,param_name="n_estimators", param_range=param_range, scoring="accuracy")
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Plot the validation curve
plt.figure(figsize=(10, 6))
plt.title("Random Forest Classifier Validation Curve")
plt.xlabel("Number of Estimators (n_estimators)")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
plt.grid()
plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.1, color="r")
plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, alpha=0.1, color="g")

plt.plot(param_range, train_mean, color="r", marker="o", markersize=5, label="Training score")
plt.plot(param_range, test_mean, color="g", marker="s", markersize=5, label="Cross-validation score")
plt.savefig('img/fig3.png')
