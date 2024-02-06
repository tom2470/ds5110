import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('data/gapminder.tsv', sep= "\t")
g=sns.FacetGrid(df,col='continent')
g.map_dataframe(sns.scatterplot,x='lifeExp',y='gdpPercap',alpha=0.3)
g.savefig('img/fig3.png')
df['gdpPercaplog']=np.log2(df['gdpPercap'])
g=sns.FacetGrid(df,col='continent')
g.map_dataframe(sns.scatterplot,x='lifeExp',y='gdpPercaplog',alpha=0.3)
g.savefig('img/fig3logbase.png')
