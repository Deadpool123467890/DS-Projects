#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\country_wise_latest.csv")
df


# In[3]:


# first five records from data set
df.head()


# In[4]:


df.columns


# In[5]:


df.info


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[18]:


# which country are mostly affected outbreak

x=df['WHO Region'].value_counts()
y=df['WHO Region'].value_counts().keys()
x


# In[17]:


# draw a pie chart for above 

plt.figure(figsize=(10,7))
plt.pie(x,labels=y,autopct="%0.1f%%")
plt.show()


# In[29]:


df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=True)


# In[26]:


# cases less than 10
df1=df[(df['Confirmed']>10)]
df1


# In[36]:


# Region with the Maximum Number of Confirmed Case

df.groupby('Country/Region')['Confirmed'].sum().head(10)


# In[40]:


#  Region with the Minimum Number of Death Cases

min_death_region = df.groupby("Country/Region")["Deaths"].sum().sort_values(ascending=True).head(10)
min_death_region


# In[ ]:




