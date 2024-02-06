import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import OneHotEncoder
df=pd.read_csv('data/diamonds.csv')
df['logarithm_base2_price'] = np.log2(df['price'])
df['logarithm_base2_carat'] = np.log2(df['carat'])
model=LinearRegression()
# Converting type of columns to category
df['color'] = df['color'].astype('category')
df['clarity'] = df['clarity'].astype('category')
df['cut'] = df['cut'].astype('category') 
  
# Assigning numerical values and storing it in another columns
df['color'] = df['color'].cat.codes
df['clarity'] = df['clarity'].cat.codes
df['cut'] = df['cut'].cat.codes
  
# Create an instance of One-hot-encoder
enc = OneHotEncoder(drop='first')
  
# Passing encoded columns
my_list=['color','clarity','cut']
for i in my_list:
  enc_data = pd.DataFrame(enc.fit_transform(np.array(df[i]).reshape(-1, 1)).toarray())
  df2=enc_data.join(df['logarithm_base2_carat'])
  Y=df['logarithm_base2_price']
  df2.columns = df2.columns.astype(str)
  cv_results = cross_validate(model, df2, Y, cv=5, scoring=('r2'),return_train_score=True)
  for train_score, test_score in zip(cv_results['train_score'], cv_results['test_score']):
    print(f"The training R2 score for {i} is {train_score}")
    print(f"The test R2 score for {i} is {test_score}")