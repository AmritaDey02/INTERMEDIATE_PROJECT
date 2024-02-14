#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
import datetime
from statistics import mean


# In[2]:


data= pd.read_csv("telecom_customer_churn.csv")


# In[3]:


data


# In[4]:


data.shape


# # MISSING VALUES

# In[6]:


data.isnull()


# In[7]:


data.info()


# In[8]:


data.describe()


# In[9]:


data.isnull().sum()


# In[10]:


data.isnull().sum().sum()


# In[11]:


data.head()


# # remove outliers

# In[16]:


sns.displot(data['Age'])


# In[17]:


sns.boxplot(data['Age'])


# In[20]:


data['Age'].mean()


# In[26]:


df=data[data['Age']<100]


# In[27]:


df['Age'].mean()


# In[28]:


df.shape


# In[29]:


df.boxplot()


# In[30]:


df.hist()


# In[ ]:





# In[ ]:





# In[ ]:




