import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('data/2020RES_APR2019PubDataShare.csv')
df2=pd.melt(df, id_vars=['SPORT_NAME'], value_vars=['APR_RATE_2019_1000','APR_RATE_2018_1000','APR_RATE_2017_1000','APR_RATE_2016_1000','APR_RATE_2015_1000','APR_RATE_2014_1000','APR_RATE_2013_1000','APR_RATE_2012_1000','APR_RATE_2011_1000','APR_RATE_2010_1000','APR_RATE_2009_1000','APR_RATE_2008_1000','APR_RATE_2007_1000','APR_RATE_2006_1000','APR_RATE_2005_1000','APR_RATE_2004_1000'])
df2['gender']=df2['SPORT_NAME'].apply(lambda x : "women" if "Women" in x else "men" if "Men" or "ball" in x else "np.nan")
df2=df2.dropna()
df2['year']=df2['variable'].apply(lambda x: x[9:13])
g=sns.violinplot(x=df2["value"])
g.set_xlabel("APR Score")
fig=g.figure
fig.savefig('img/fig0.png')
df2=df2[df2["value"]>850]
df2.to_csv("data/my_data.csv",index=False)
print(df2.head())