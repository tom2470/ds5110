import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('data/gapminder.tsv', sep= "\t")
g=sns.FacetGrid(df,col='year', col_wrap=3)
g.map_dataframe(sns.boxplot,x='lifeExp',y='continent', hue='continent')
g.savefig('img/fig2.png')
