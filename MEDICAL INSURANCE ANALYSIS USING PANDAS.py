#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # to import csv file using read fuction
# 

# In[2]:


df=pd.read_csv("C:\medical_insurance.csv")
df


# # to find top 5 rows using head function

# In[3]:


df.head(5)


# # to know about dataset we use describe func

# In[4]:


df.describe()


# # to know about data set we use info fuction

# In[5]:


df.info()


# # to know about columns and rows using shape fuction

# In[6]:


df.shape


# # to find null values using is null

# In[7]:


df.isnull().sum()


# # to know how much male and female exist we use value_counts function

# In[8]:


df['sex'].value_counts()


# # to find unique values in data we use unique fuction

# In[9]:


df['sex'].unique()


# # to replace data using replace fuction

# In[10]:


df['sex']=df['sex'].replace('female','womens')


# # SEX COLUMN

# In[11]:


df['sex'].value_counts()


# In[12]:


df['sex']=df['sex'].replace('male','men')


# In[13]:


df['sex'].value_counts()


# In[14]:


df.groupby('sex').sum()


# In[17]:


plt.figure(figsize=(4,3))
sns.countplot(x="sex",data=df)
plt.title("count of sex")
plt.show()


# # REGION COLUMNS

# In[18]:


df["region"].value_counts()


# In[19]:


x=df["region"].value_counts().index
y=df["region"].value_counts().values
x
y


# In[33]:


plt.pie(y,labels=x,startangle=60,autopct="%0.2ff")
plt.legend(loc=3)
plt.show()


# In[41]:


plt.figure(figsize=(4,3))
sns.countplot(x="region",data=df,hue="smoker")
plt.title("count of region")
plt.show()


# # smoke columns

# In[36]:


plt.figure(figsize=(4,3))
sns.countplot(x="smoker",data=df)
plt.title("count of smoker")
plt.show()


# In[47]:


plt.figure(figsize=(4,3))
sns.countplot(x="region",data=df[df['region']=='southwest'],hue="smoker")
plt.title("count of region")
plt.show()


# # children columns

# In[42]:


df['children'].value_counts()


# In[43]:


plt.figure(figsize=(4,3))
sns.countplot(x="sex",data=df,hue="children")
plt.title("count of children")
plt.show()


# In[44]:


x=df["children"].value_counts().index
y=df["children"].value_counts().values
x
y


# In[46]:


plt.pie(y,labels=x,startangle=60,autopct="%0.2f")
plt.legend(loc=3)
plt.show()


# In[ ]:





# In[ ]:




