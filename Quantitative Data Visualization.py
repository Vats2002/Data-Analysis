#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np


# In[7]:


listings = pd.read_csv('listings.csv')


# In[4]:


listings


# In[8]:


plt.hist(listings['price'])
plt.xlabel('price(in US Dollars)')
plt.show()


# In[10]:


plt.hist(listings['price'], bins = np.arange(0,1100,40))
plt.xlabel('price(in US Dollars)')
plt.show()


# In[12]:


plt.scatter(x = listings['price'], y = listings ['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.show()


# In[14]:


plt.scatter(x = listings['price'], y = listings ['number_of_reviews'])
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0,1100)
plt.show()


# In[16]:


plt.scatter(x = listings['price'], y = listings ['number_of_reviews'], s = 5)
plt.xlabel('price')
plt.ylabel('number of reviews')
plt.xlim(0,1100)
plt.show()


# In[ ]:




