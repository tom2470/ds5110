import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('data/gapminder.tsv', sep= "\t")
df2=df.groupby(['country']).mean()
df3=df[['country','continent']].drop_duplicates()
df2 = pd.merge(df2,df3,on='country', how='left')
d = {'color': [ 'b','purple','g','r','y']}
g=sns.FacetGrid(df,col='continent',margin_titles=True, despine=False, hue_kws=d, hue='continent')
g.map_dataframe(sns.histplot,x='lifeExp')
g.figure.subplots_adjust(wspace=0, hspace=0)
'''
g=sns.FacetGrid(df,col='year')
g.map_dataframe(sns.histplot,x='lifeExp', hue= 'continent',multiple="stack",legend=True, palette="pastel").add_legend();
'''
g.savefig('img/fig1.png')