import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.express as px


df=pd.read_csv('data/diamonds.csv')
a=px.histogram(df, x='price')
a.write_image("figs/fig21.png")
# print(type(a))
# fig=a.get_figure()
# fig.show()
# fig.savefig('figs/figure21.png')


df['logarithm_base2_price'] = np.log2(df['price'])
b=px.histogram(df, x='logarithm_base2_price')
b.write_image("figs/fig22.png")
# print(type(b))
# fig2=b.get_figure()
# print(type(fig2))
# fig2.show()
# fig2.savefig('figs/figure22.png')


e=px.histogram(df, x='carat')
e.write_image("figs/fig23.png")
# fig3=e.get_figure()
# fig3.show()
# fig3.savefig('figs/figure23.png')


df['logarithm_base2_carat'] = np.log2(df['carat'])
c=px.histogram(df, x='logarithm_base2_carat', nbins=15)
c.write_image("figs/fig24.png")
# fig4=c.get_figure()
# fig4.savefig('figs/figure24.png')


d=px.scatter(df, x='logarithm_base2_carat', y='logarithm_base2_price')
d.write_image('figs/figure25.png')
