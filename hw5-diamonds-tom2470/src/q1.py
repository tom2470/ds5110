import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('data/diamonds.csv')
g=sns.scatterplot(data=df, x='carat', y='price')
plt.savefig('figs/figure11.png')