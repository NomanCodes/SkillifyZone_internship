# -*- coding: utf-8 -*-
"""Week 1: Data Understanding & Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18BZCGa0dOnGFIflrXzibaUy0pd5aLlaZ
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/Sample - Superstore.csv' , encoding='latin-1')

df.shape  #to check rows and columns

df.isnull().sum() #to check null values

df.head(2)

#category sells best
category_sales=df.groupby('Category')['Sales'].sum()
category_sales

#region earns the most
region_sales=df.groupby('Region')['Sales'].sum()
region_sales

#plotting

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Total Profit by Region")
plt.ylabel("Profit")
plt.xlabel("Region")
plt.show()