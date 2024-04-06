#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\ipl data (1).csv")
df


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df['id'].unique()


# In[8]:


df['season'].unique()


# In[9]:


df['city'].unique()


# In[10]:


df['date'].unique()


# In[11]:


df['team1'].unique()


# In[12]:


df['team2'].unique()


# In[13]:


df['toss_winner'].unique()


# In[14]:


df['toss_decision'].unique()


# In[15]:


df['result'].unique()


# In[16]:


df['dl_applied'].unique()


# In[17]:


df['winner'].unique()


# In[18]:


df['win_by_runs'].unique()


# In[19]:


df['win_by_wickets'].unique()


# In[20]:


df['player_of_match'].unique()


# In[21]:


df['venue'].unique()


# In[22]:


df['umpire1'].unique()


# In[23]:


df['umpire2'].unique()


# In[24]:


df.isnull().sum()/len(df)*100


# In[25]:


df.drop(['umpire3'],axis=1,inplace=True)


# In[26]:


df.dropna(inplace=True)


# In[27]:


df.isnull().sum()


# In[28]:


#which city hosted most number of matches?
#draw bar plot and write down your insights

a=df['city'].value_counts()
b=df['city'].value_counts().keys()

plt.figure(figsize=(10,10))
plt.bar(b,a,color='g')
plt.show()


# In[29]:


#find all venue of mumbai city

Venue_Mum=df[df['city']=='Mumbai'][['venue']]
a=Venue_Mum['venue'].unique()
a


# In[30]:


b=df[df['city']=='Mumbai'][['venue']].value_counts()
b


# In[31]:


b.plot(kind='bar', figsize=(10, 6), color='g', alpha=0.7)


# In[32]:


#what is the preferred choice after winning a toss in mumbai

Toss_win_Mum=df[df['city']=='Mumbai'][['toss_decision']].value_counts()
Toss_win_Mum


# In[33]:


Toss_win_Mum.plot(kind='bar', figsize=(10, 6), color='g', alpha=0.7)


# In[34]:


toss_win=df['toss_winner'].value_counts()


# In[35]:


toss_win.plot(kind='bar', figsize=(10, 6), color='g', alpha=0.7)


# In[36]:


#find what mumbai indians preferred after winning a toss?

df[df['toss_winner']=='Mumbai Indians']['toss_decision'].value_counts()


# In[37]:


#head to head winning count of Mumbai Indians vs Chennai Super Kings

import pandas as pd

# Assuming you have a DataFrame named 'match_results' with columns 'Team1', 'Team2', and 'Winner'
# Example DataFrame structure:
# match_results = pd.DataFrame({'Team1': [...], 'Team2': [...], 'Winner': [...]})

# Filter matches involving Mumbai Indians and Chennai Super Kings
mi_csk_matches = df(df['team1']=='Mumbai Indians')&(df['team2'] == 'Chennai Super Kings')|((df['team1']=='Chennai Super Kings') & (df['team2'] =='Mumbai Indians'))

# Calculate head-to-head winning count
head_to_head_count = mi_csk_matches['winner'].value_counts()

# Display the head-to-head winning count
print(head_to_head_count)


# In[38]:


mum_city_won=df[df['city']=='Mumbai'][['winner']].value_counts()


# In[39]:


mum_city_won


# In[54]:


#how many times each team won the toss and won the match

won_toss=df.groupby(['toss_winner','winner'])[['city']=='Mumbai'].size().reset_index(name='count')


# In[55]:


result=won_toss[won_toss['toss_winner']==won_toss['winner']]


# In[66]:


#how many times each team won the toss and won the match in mumbai

Mumbai_match=df[df['city']=='Mumbai']
toss_winner= Mumbai_match[Mumbai_match['toss_winner']==Mumbai_match['winner']]['toss_winner'].value_counts()
toss_winner


# In[67]:


#which venue hosted most number of matches

most_venue=df['venue'].value_counts()


# In[68]:


most_venue.plot(kind='bar', figsize=(10, 6), color='g', alpha=0.7)


# In[75]:


#find how many matches chennai super kings played at M Chinnaswamy stadium?
result=m_chinna_std[(m_chinna_std['team1']=='Chennai Super Kings')|(m_chinna_std['team2']=='Chennai Super Kings')]

result=result[result['venue']=='M Chinnaswamy Stadium'].value_counts()
number_matches=len(result)


# In[77]:


number_matches


# In[79]:


#who won most matches at M Chinnaswamy stadium?

most_won=df[df['venue']=='M Chinnaswamy Stadium']
result=most_won['winner'].value_counts()
result


# In[92]:


#matches played in each year

most_match_year=df[df['season']=='2013']['city'].value_counts()


# In[94]:


most_match_year


# In[ ]:





# In[ ]:




