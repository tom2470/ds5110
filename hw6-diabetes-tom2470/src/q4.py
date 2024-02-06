import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.datasets import load_diabetes

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.datasets import load_diabetes

data = load_diabetes()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
n_components = np.arange(1, X.shape[1] + 1)
trainscores = []
testscores = []

for n in n_components:
    pca = PCA(n_components=n)
    X_train_pca = pca.fit_transform(X_train)
    reg = LinearRegression()
    cv_train_scores = cross_val_score(reg, X_train_pca, y_train, cv=5)
    trainscores.append(np.mean(cv_train_scores))
    X_test_pca = pca.transform(X_test)
    cv_test_scores = cross_val_score(reg, X_test_pca, y_test, cv=5)
    testscores.append(np.mean(cv_test_scores))


plt.figure()
plt.plot(n_components, trainscores, label='Training Scores')
plt.plot(n_components, testscores, label='Test Scores')
plt.title('CVS vs PCP')
plt.xlabel('Number of Components')
plt.ylabel('Cross Validation Score')
plt.legend()
plt.savefig('img/fig4.png')
