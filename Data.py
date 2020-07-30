#!/usr/bin/env python
# coding: utf-8

# In[27]:


import locale

# import import_ipynb
import pandas as pd

# Read Data
# In[57]:
locale.setlocale(locale.LC_ALL, '')
print(locale.getdefaultlocale(['LC_ALL']))
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.min_rows', 20)
pd.options.display.min_rows = 30
pd.options.display.max_rows = 30
data = pd.read_csv('./Exple.csv', sep=";", parse_dates=['Date'])
index = pd.date_range(start='1/1/2020', periods=8784, freq='1h00t')
data['time'] = index
data.set_index('time', inplace=True)
data['FDate'] = pd.to_datetime(data['Date'])
data['day_of_week'] = data['FDate'].dt.day_name()

data.drop(['Date', 'Heures'], axis=1, inplace=True)

# In[58]:
from IPython.display import display

week_df = data.groupby(data['FDate'].dt.day_name()).mean()
display(week_df)

# In[59]:




with pd.option_context('display.min_rows', 30, 'display.max_rows', 30, 'display.max_columns', 20):
    display(data)

# In[17]:


# Solar park installed in 2020 = 10020
data['Solaire_kwh'] = data['Solaire'] / 10020

# In[ ]:
