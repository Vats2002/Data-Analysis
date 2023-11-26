#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


listings = pd.read_csv('listings.csv')


# In[19]:


listings


# In[20]:


sns.countplot(x='neighbourhood_group', data=listings)
plt.xlabel('Neighbourhood Group')
plt.ylabel('Count')
plt.title('Count of Listings by Neighbourhood Group')
plt.show()


# In[9]:


listings


# In[23]:


sns.countplot(x='neighbourhood_group', data=listings)
plt.xlabel('Neighbourhood Group')
plt.show()


# In[24]:


sns.countplot(x='neighbourhood_group', data=listings)
plt.show


# In[ ]:




