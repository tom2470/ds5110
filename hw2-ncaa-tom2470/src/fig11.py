import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df2=pd.read_csv("data/my_data.csv")
sns.set(rc={"figure.figsize":(10, 5)})
k=sns.boxplot(data=df2, x="year", y="value")
k.set_ylabel("APR Score")
k.set_title("APR Score Distrubution \nOver years")
fig=k.figure
fig.savefig('img/fig1.png')