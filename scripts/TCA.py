#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'c:\Users\Zeba\Desktop\churn.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.sample(5)


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.shape


# In[9]:


df.describe()


# In[10]:


df.isnull().sum()


# In[11]:


df.duplicated().sum()


# In[12]:


df["gender"].value_counts()


# In[13]:


df.dtypes


# In[14]:


df.nunique()


# In[15]:


df.describe(include="all")


# In[16]:


df["InternetService"].unique()


# In[17]:


df["Contract"].unique()


# In[20]:


plt.figure(figsize=(4,4))
ax=sns.countplot(x='Churn',data=df)
ax.bar_label(ax.containers[0])
plt.title('count Churn')
plt.ylabel('count of Customers')


# In[24]:


plt.figure(figsize=(3,4))
sns.countplot(x="gender",data=df,hue="Churn")
plt.title("Customers")


# In[28]:


plt.figure(figsize=(3,4))
sns.countplot(x="SeniorCitizen",data=df,hue="Churn")
plt.title("SeniorCitizen")


# In[29]:


plt.figure(figsize=(3,4))
ax=sns.countplot(x="SeniorCitizen",data=df)
plt.title("count of Total seniorcitizen")


# In[32]:


plt.figure(figsize=(4,4))
sns.countplot(x="Contract",data=df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("based on contract")
plt.xlabel("type of contract")
plt.ylabel("count of customers")


# In[33]:


plt.figure(figsize=(4,4))
sns.countplot(x="PhoneService",data=df)
plt.title("Phone service")


# In[36]:


plt.figure(figsize=(4,4))
sns.countplot(x="InternetService",data=df)
plt.title("internet service")
plt.xlabel("Types of internet service")
plt.ylabel("count of customers")


# In[38]:


plt.figure(figsize=(4,4))
sns.countplot(x="MultipleLines",data=df)
plt.title("Multiplelines")
plt.ylabel("count of customers")
plt.xlabel("Types of lines")


# In[40]:


plt.figure(figsize=(4,4))
sns.countplot(x="OnlineSecurity",data=df)
plt.title("Online security")
plt.xlabel("Types of Security")
plt.ylabel("count of customers")


# In[43]:


plt.figure(figsize=(4,4))
sns.countplot(x="OnlineBackup",data=df)
plt.title("online backup")


# In[44]:


plt.figure(figsize=(4,4))
sns.countplot(x="DeviceProtection",data=df)
plt.title("Device protection")


# In[45]:


plt.figure(figsize=(4,4))
sns.countplot(x="TechSupport",data=df)
plt.title("Tech support")


# In[49]:


plt.figure(figsize=(4,4))
sns.countplot(x="StreamingTV",data=df)
plt.title("streamingtv")


# In[54]:


plt.figure(figsize=(4,4))
sns.countplot(x="StreamingMovies",data=df)
plt.title("Streaming movies")


# In[55]:


plt.figure(figsize=(4,4))
sns.countplot(x="PaperlessBilling",data=df)
plt.title("Paperlessbilling")


# In[57]:


sns.countplot(x="PaymentMethod",data=df)


# In[ ]:




