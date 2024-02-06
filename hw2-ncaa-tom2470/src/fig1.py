import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df2=pd.read_csv("data/my_data.csv")
colors = ['#030303']
colors_boxplot = dict(color=colors[0])
medians = df2['value'].median()
vertical_offset = df2['value'].median() * 0.001
sns.set(style="darkgrid")
g = sns.FacetGrid(df2, col="year", col_wrap=4)
g.map_dataframe(sns.violinplot, y="value",color='skyblue', inner=None)
g.map_dataframe(sns.boxplot, y="value", saturation=1, showfliers=False, width=0.1, boxprops={'zorder': 3 , 'color':colors[0],'facecolor': 'none'},  medianprops=colors_boxplot, whiskerprops=colors_boxplot, capprops=colors_boxplot, flierprops=dict(markeredgecolor=colors[0]))
g.set_ylabels("APR Score")
g.set_titles('{col_name}')
g.savefig('img/fig1.png')