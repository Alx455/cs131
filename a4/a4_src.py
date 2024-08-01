# -*- coding: utf-8 -*-
"""CS131 as04.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oKwizedebKx4N4pVprEMMrw16_lLgCDi
"""

!pip install ucimlrepo

from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import matplotlib.pyplot as plt

# TARGET VARIABLE = 'quality'

WHITE_WINE_CSV = '/content/winequality-white.csv'
white_wine_df = pd.read_csv(WHITE_WINE_CSV, sep=';')

#white_wine_df.head(5)

# Question 1
print(white_wine_df.astype(int).describe())


# Question 2
plt.matshow(white_wine_df.corr())
plt.title('Correlation Matrix of Wine Quality - White Dataset')
plt.show


# Question 3
ax = (white_wine_df['quality']).plot.hist()
ax.set_xlabel('quality')
ax.set_ylabel('frequency')
ax.set_title('Distribution of Wine Quality')
ax.set_xlim(0, 10)
plt.show()


# Question 4
features = white_wine_df.columns.drop('quality')
for i, feature in enumerate(features):
  plt.subplot(6, 2, i+1)
  sns.violinplot(data=white_wine_df, x = 'quality', y = feature)
  plt.xlabel('Quality')
  plt.ylabel(feature)
  plt.title(f'{feature} vs Quality')
  plt.show()


# Question 5
model = LinearRegression()
model.fit(white_wine_df[['alcohol']], white_wine_df['quality'])

fitted = model.predict(white_wine_df[['alcohol']])
RMSE = np.sqrt(mean_squared_error(white_wine_df['quality'], fitted))
r2 = r2_score(white_wine_df['quality'], fitted)

print(f'b0 = {model.intercept_}')
print(f'b1 = {model.coef_[0]}')
print(f'RMSE = {RMSE}')
print(f'r2 = {r2}')


# Question 6
model = LinearRegression()
model.fit(white_wine_df[['volatile acidity', 'alcohol', 'density']], white_wine_df['quality'])

fitted = model.predict(white_wine_df[['volatile acidity', 'alcohol', 'density']])
RMSE = np.sqrt(mean_squared_error(white_wine_df['quality'], fitted))
r2 = r2_score(white_wine_df['quality'], fitted)

print(f'b0 = {model.intercept_}')
print(f'Coef for volatile_acidity: b1 = {model.coef_[0]}')
print(f'Coef for alcohol: b2 = {model.coef_[1]}')
print(f'Coef for density: b3 = {model.coef_[2]}')
print(f'RMSE = {RMSE}')
print(f'r2 = {r2}')