import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import datasets
from sklearn.linear_model import Lasso
import numpy as np

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Perform Lasso regression path
alphas = np.logspace(-4, 4, 100)
coefs = []

for a in alphas:
    lasso = Lasso(alpha=a)
    lasso.fit(X, y)
    coefs.append(lasso.coef_)

# Plot the coefficients
plt.figure()
colors = cycle(['red', 'blue', 'green', 'black', 'orange'])  # Add more colors if needed

for coef, color in zip(np.array(coefs).T, colors):
    plt.plot(np.log10(alphas), coef, color=color)

plt.xlabel('Log(alpha)')
plt.ylabel('Coefficients')
plt.title('Lasso Paths of Diabetes Coefficients')
plt.axis('tight')

# Add a legend with feature names
feature_names = diabetes.feature_names
plt.legend(feature_names, loc='upper right')

plt.savefig('img/fig5.png')