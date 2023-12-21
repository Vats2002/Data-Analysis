#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[3]:


diabetes = pd.read_csv('diabetes.csv')


# In[20]:


diabetes


# In[21]:


sns.heatmap(diabetes.isnull())


# In[22]:


correlation = diabetes.corr()
print(correlation)


# In[23]:


plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[27]:


X =diabetes.drop("outcome",axis=1)
Y =diabetes['outcome']
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size =0.2)


# In[28]:


import train_test_split


# In[33]:


import pandas as pd
from sklearn.model_selection import train_test_split


# In[35]:


X = diabetes.drop("outcome", axis=1)
Y = diabetes['outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# In[ ]:




