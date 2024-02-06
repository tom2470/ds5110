import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df2=pd.read_csv("data/my_data.csv")
g=sns.displot(df2, x="value", col="SPORT_NAME",binwidth=10, height=3, facet_kws=dict(margin_titles=True),col_wrap=5)
g.map(lambda x, **kw: plt.axvline(x.mean(), color="green",ls='--',lw=0.5, label="sport mean"), 'value')
g.map(plt.axvline,x=df2[df2["gender"]=='men']['value'].mean(),color='blue',ls='--', lw=0.5, label="men sports mean")
g.map(plt.axvline,x=df2[df2["gender"]=='women']['value'].mean(),color='red',ls='--', lw=0.5, label="womens sports mean")
g.set_xlabels("APR Score")
g.set_ylabels("Amount of Teams")
custom_colnames = df2['SPORT_NAME'].unique()
# for i, ax in enumerate(g.axes[0]):
#     ax.set_title(custom_colnames[i], fontsize=10)
plt.legend(bbox_to_anchor=(1.25, 1), borderaxespad=0)
g.savefig('img/fig3.png')