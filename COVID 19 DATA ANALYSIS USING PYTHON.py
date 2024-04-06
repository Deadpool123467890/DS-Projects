#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("C:\Covid data.csv")
df


# In[5]:


df.columns


# In[6]:


df.shape


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.isnull().sum()


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


df.count()


# In[14]:


df['Date'].unique()


# In[15]:


df['State'].unique()


# In[16]:


df['Region'].unique()


# In[17]:


df['Confirmed'].unique()


# In[18]:


df['Deaths'].unique()


# In[19]:


df['Recovered'].unique()


# In[23]:


Region=df['Region'].value_counts()
Region


# In[28]:


df.groupby('Region').sum().head(50)


# In[44]:


df.groupby('Region')['Confirmed'].sum()


# In[31]:


df.groupby('Region')['Deaths'].sum().head(50)


# In[32]:


df.groupby('Region')['Recovered'].sum().head(50)


# In[36]:


less_10=df[df['Confirmed']<=10]
less_10


# In[37]:


df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)


# In[39]:


df.groupby('Region')['Deaths'].sum().sort_values(ascending=True)


# In[45]:


df[df['Region']=='Canada']


# In[ ]:




