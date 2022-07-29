#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Pandas is an open source 


# In[2]:


# importing pandas 
import pandas as pd
import numpy as np


# In[3]:


""" DataFrame. DataFrame is a 2-dimensional labeled data structure
with columns of potentially different types.
You can think of it like a spreadsheet or SQL table,
or a dict of Series objects. It is generally the most
commonly used pandas object. """


# In[11]:


# Creating data frame:

df=pd.DataFrame(np.arange(0,20).reshape(5,4), index=['row1', 'row2', 'row3', 'row4','row5'],columns=['col1', 'col2', 'col3', 'col4'])


# In[6]:


df.head()


# In[7]:


df.to_csv('test1.csv')


# In[16]:


# Accessing the element 
# 1. .loc 2. .iloc

df.loc['row1']


# In[17]:


type(df.loc['row1'])


# In[20]:


#using iloc
df.iloc[0:2,0:2]


# In[21]:


# now here if we want to see the type of above data it will be a Data Frame 
type(df.iloc[0:2,0:2])


# In[ ]:


# even if we have single colomn but if it is in above format then it is Data Frame.


# In[23]:


# Converting data frame into arrays: (use .values)
df.iloc[:,:].values


# In[24]:


# to see shape of an array
df.iloc[:,:].values.shape


# In[25]:


#how to check null condition:
df.isnull().sum()


# In[ ]:


#The value_counts() function is used to get a Series containing counts of unique values.


# In[26]:


df['col1'].value_counts()


# In[27]:


df['col1'].unique()


# In[30]:


# we can even access the elements without loc or iloc 
# if we want ot access multiple row we haveto pass it in the form of list 
df[['col1', 'col2']]


# In[31]:


df.head()


# In[ ]:




