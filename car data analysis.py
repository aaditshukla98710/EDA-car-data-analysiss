#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns  
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


hello =pd.read_csv('https://raw.githubusercontent.com/rajtilakls2510/car_price_predictor/master/quikr_car.csv')
hello.head()


# In[4]:


hello.shape


# In[5]:


hello.info()


# In[6]:


hello.describe()


# In[7]:


hello['year'].unique()


# In[8]:


hello['year'].value_counts()


# In[9]:


hello['Price'].unique()


# In[10]:


hello['Price'].nunique()


# In[11]:


hello['Price'].value_counts()


# In[12]:


hello.isnull().sum()


# In[13]:


hello['kms_driven'].isna()


# In[14]:


hello=hello[hello['year'].str.isnumeric()]
hello.head()


# In[15]:


hello['year']=hello['year'].astype(int)
hello['year']


# In[16]:


hello.info()


# In[17]:


hello['year'].unique()


# In[18]:


hello['Price'].unique()


# In[19]:


hello=hello[hello['Price']!='Ask For Price']
hello.head()


# In[20]:


hello['Price']=hello['Price'].str.replace(',','').astype(int)
hello['Price']


# In[21]:


hello.info()


# In[22]:


hello['kms_driven'].isnull().sum()


# In[23]:


hello.isnull().sum()


# In[24]:


hello['kms_driven'].value_counts()


# In[25]:


hello['kms_driven'].str.isnumeric()


# In[ ]:





# In[ ]:





# In[26]:


hello['kms_driven']=hello['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
hello['kms_driven']


# In[27]:


hello=hello[hello['kms_driven'].str.isnumeric()]
hello.head()


# In[28]:


hello['kms_driven']=hello['kms_driven'].astype(int)
hello['kms_driven']


# In[29]:


hello.info()


# In[30]:


hello['kms_driven'].isnull().sum()


# In[31]:


hello=hello[~hello['fuel_type'].isna()]
hello.head()


# In[32]:


hello['company'].value_counts().sum()


# In[33]:


hello['company'].unique()


# In[34]:


hello['company']


# In[35]:


hello.describe()


# In[36]:


sns.distplot(hello['year'],kde=False,bins=4)


# In[37]:


sns.kdeplot(data=hello['Price'],label="Price",shade=True)


# In[38]:


hello['Price'].hist(bins=16)


# In[39]:


hello['company'].value_counts().plot(kind='bar',figsize=[10,6])


# In[40]:


sns.stripplot(x=hello['fuel_type'])


# In[ ]:





# In[41]:


ax = sns.violinplot(x="year", y="company", data=hello,figsize=[13,12])


# In[42]:


sns.pairplot(data=hello,hue='year')


# In[48]:


sns.boxplot(x='year',y='company',hue='Price',data=hello)


# In[49]:


sns.boxplot(x='year',y='fuel_type',hue='company',data=hello)


# In[ ]:





# In[ ]:





# In[ ]:




