import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
param_grid = {'C': [0.1, 1, 10, 100, 1000],'gamma': [0.001, 0.01, 0.1, 1]}
grid = GridSearchCV(svc, param_grid)
grid.fit(X_train, y_train)
print("Optimal Hyperparameters:", grid.best_params_)
y_pred = grid.predict(X_test)

target_names = [str(i) for i in digits.target_names]
print(classification_report(y_test, y_pred, target_names=target_names))

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap='Blues', cbar=False,xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig('img/fig5.png')