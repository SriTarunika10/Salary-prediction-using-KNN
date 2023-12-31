# -*- coding: utf-8 -*-
"""KNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsTj0TV8y2RJkVhAbz9h9Bgzhek7W9cX
"""

import numpy as np
import pandas as pd

df=pd.read_csv("/content/salary_predict_dataset.csv")

df

#head
df.head()

#tail
df.tail()

#shape
df.shape

#columns
df.columns

#size
df.size

#info
df.info()

#describe
df.describe

#isnull
df.isnull()

#total null values
df.isnull().sum()

df["experience"] = pd.to_numeric(df["experience"], errors='coerce')

df["experience"].mean()

df["test_score"].mean()

df["interview_score"].mean()

#filling the null values using fillna
df["experience"]=df["experience"].fillna(7.0)
df["test_score"]=df["test_score"].fillna(5.175)
df["interview_score"]=df["interview_score"].fillna(5.375)

df["experience"].mean()

df.head()

df.isnull()

df.head()

#sns.heatmap(df.corr(),cmap="crest",annot=True)

sns.barplot(x=df['experience'],y=df['test_score'])

sns.barplot(x=df['experience'],y=df
 ['interview_score'])

sns.jointplot(x=df['test_score'],y=df['interview_score'])

#assigning the variable
X1=df["test_score"]
X2=df["interview_score"]
X=X1,X2
y=df["Salary"]

from sklearn.model_selection import train_test_split

# Assigning the variables
X1 = df["test_score"]
X2 = df["interview_score"]
X = df[["test_score", "interview_score"]]  # Combine both features into one DataFrame
y = df["Salary"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=102)

print(X.shape)

print(y.shape)

#train_test_split
from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=102)

print(X_train.shape)

print(y_train.shape)

print(X_test.shape)

print(y_test.shape)

from sklearn import neighbors
from sklearn.metrics import mean_squared_error,r2_score

model = neighbors.KNeighborsRegressor(n_neighbors = 5)
model.fit(X_train, y_train)  #fit the model

y_pred=model.predict(X_test)

print(pred)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

#r2_score
r2 = r2_score(y_test, y_pred)

print(f"R-squared (R^2): {r2}")

