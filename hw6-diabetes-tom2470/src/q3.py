import seaborn as sns
from sklearn import datasets
import matplotlib.pyplot as plt
diabetes = datasets.load_diabetes(as_frame=True)
data=diabetes.data
sns.heatmap(data.corr(method ='pearson'),cmap='coolwarm',annot=True)
plt.savefig('img/fig3.png')