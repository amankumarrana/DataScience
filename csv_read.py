#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:38:03 2018

@author: amanrana
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sample-salesv2.csv', parse_dates=['date'])
sales.head()
print sales.describe()
print sales['unit price'].describe()
print sales.dtypes

customers = sales[['name', 'ext price' ,'date']]
print customers.head()
customer_group = customers.groupby('name')
print customer_group.size()
sales_total = customer_group.sum()
print sales_total.sort(columns='ext price').head()
sales_total.plot(kind='bar')
my_plot = sales_total.sort(columns='ext price',ascending=False).plot(kind='bar',legend=None,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales ($)")

# Now, let’s try to see how the sales break down by category.

customers = sales[['name' , 'category' , 'ext price', 'date']]
customers.head()
category_group = customers.groupby(['name', 'category']).sum()
print category_group.head()
category_group.unstack().head()
my_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer")
my_plot.set_xlabel('Customers')
my_plot.set_ylabel('Sales')

# In order to clean this up a little bit, we can specify the figure size and customize the legend.

my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales")
my_plot.legend(["Total","Belts","Shirts","Shoes"], loc=9,ncol=4)

purchase_patterns = sales[['ext price','date']]
purchase_patterns.head()
purchase_plot = purchase_patterns['ext price'].hist(bins=20)
purchase_plot.set_title("Purchase Patterns")
purchase_plot.set_xlabel("Order Amount($)")
purchase_plot.set_ylabel("Number of orders")

purchase_plot = purchase_patterns.resample('M',how=sum).plot(title="Total Sales by Month",legend=None)




