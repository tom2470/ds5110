import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
df=pd.read_csv('data/gapminder.tsv', sep= "\t")
myplt=sns.histplot(data=df,x='lifeExp', stat='density',kde=True,label='data')
mu, std = norm.fit(df['lifeExp'])
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)   
myplt.plot(x, p, 'k', linewidth=2, label='normal')                                               
myplt.legend()
fig=myplt.figure
fig.savefig('img/fig4.png')