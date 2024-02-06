import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df2=pd.read_csv("data/my_data.csv")
#sns.set(rc={"figure.figsize":(14, 8)})
k=sns.boxplot(data=df2, x="SPORT_NAME", y="value")
k.set_ylabel("APR Score")
k.set_title("APR Score Distrubution \nAcross Sports")
k.set_xticklabels(k.get_xticklabels(),rotation=90)
fig=k.figure
fig.savefig('img/fig3.png')