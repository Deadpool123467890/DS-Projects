#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\ipl data.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


del df['umpire3']


# In[9]:


df.isnull().sum()


# In[10]:


df.dropna(subset=['city','winner','player_of_match','umpire1','umpire2'],how='any',inplace=True)


# In[11]:


df


# In[12]:


df.isnull().sum()


# In[13]:


# number of rows and columns in data set

df.shape


# In[14]:


# most man of the match awards

df['player_of_match'].value_counts()


# In[15]:


# top 10 players with man of the match awards

x=list(df['player_of_match'].value_counts()[0:10])


# In[16]:


y=list(df['player_of_match'].value_counts()[0:10].keys())


# In[17]:


# draw bar plot of most man of the match awards

plt.figure(figsize=(10,10))
plt.bar(y,x,color='g')
plt.show()


# In[18]:


# getting the frequecy of result column

df['result'].value_counts()


# In[19]:


# no of toss win w.r.t.each team

df['toss_winner'].value_counts()


# In[20]:


# teams win match using batting first

batting_first=df[df['win_by_runs']!=0]


# In[21]:


batting_first.head()


# In[22]:


# drwing a histogram of teams win match using batting first

plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.title("teams win match using batting first")
plt.show()


# In[23]:


#finding out number of wins after batting first 

y=list(batting_first['winner'].value_counts()[0:3].keys())
y


# In[24]:


# team most win after batting 

x=list(batting_first['winner'].value_counts()[0:3])


# In[25]:


# plot bar plot of top 3 team most win after batting 

plt.figure(figsize=(10,5))
plt.bar(y,x,color=['blue','yellow','orange'])
plt.show()


# In[26]:


y=list(batting_first['winner'].value_counts()[0:3].keys())
x=list(batting_first['winner'].value_counts()[0:3])


# In[27]:


# making a pie chart of top 3 team most win after batting 

plt.figure(figsize=(10,7))
plt.pie(x,labels=y,autopct="%0.1f%%")
plt.show()



# In[28]:


# extracting those record whos team won after choose batting second

batting_second=df[df['win_by_wickets']!=0]
batting_second


# In[29]:


# draw histogram w.r.t above records

plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.title("teams win match using batting second")
plt.show()


# In[30]:


# number of frequency each time w.r.t. wickets

x=batting_second['winner'].value_counts()[0:3].keys()
x




# In[31]:


y=batting_second['winner'].value_counts()[0:3]
y


# In[32]:


# draw a bar plot of top 3 teams who won after batting second 

plt.figure(figsize=(10,5))
plt.bar(x,y,color=['red','blue','black'])
plt.show()


# In[33]:


# making pie chart for above records

plt.figure(figsize=(10,7))
plt.pie(y,labels=x,autopct="%0.1f%%")
plt.show()


# In[34]:


# match played in each season

df['season'].value_counts()


# In[35]:


# match played in each city

df['city'].value_counts()


# In[36]:


# find out how many times a team has won after winning toss

np.sum(df['toss_winner']==df['winner'])


# In[74]:





# In[ ]:





# In[ ]:




