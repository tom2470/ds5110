import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df2=pd.read_csv("data/my_data.csv")
sns.set(rc={"figure.figsize":(10, 5)})
k=sns.boxplot(data=df2, x="year", y="value", hue="gender")
k.set_ylabel("APR Score")
k.set_title("APR Score Distrubution \nFemale vs Male Sports")
fig=k.figure
fig.savefig('img/fig2.png')
