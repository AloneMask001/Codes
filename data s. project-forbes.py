#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd; import numpy as np


# In[2]:


df=pd.read_csv("forbes.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df=df.loc[:,['rank', 'personName', 'age', 'finalWorth','category','country','gender'
            ]]
df.head()


# In[7]:


df=df.rename(columns={'rank':"sıra",'personName':"isim",'age':"yaş",'finalWorth':"servet",'category':"kategori",'country':"ülke",'gender':"cinsiyet"})


# In[8]:


df=df.set_index("sıra")
df.head()


# In[9]:


df.head()


# In[10]:


df.dtypes


# In[11]:


df.isnull().sum()


# In[12]:


df.dropna(inplace=True)


# In[13]:


df.isnull().sum()


# In[14]:


df.shape


# In[15]:


df["cinsiyet"].value_counts()


# In[16]:


(df["cinsiyet"].value_counts(normalize=True)*100)


# In[17]:


df[df["ülke"]=="Turkey"].cinsiyet.value_counts(normalize=True)


# In[18]:


df["ülke"].unique()


# In[19]:


(df[df["ülke"]=="Canada"].cinsiyet.value_counts(normalize=True)*100)


# In[20]:


df_cinsiyet = df.groupby(["cinsiyet"])
df_cinsiyet["yaş"].mean()


# In[21]:


import seaborn as sns
sns.set_theme()
sns.set(rc={"figure.dpi":300})
import warnings
warnings.filterwarnings("ignore")


# In[22]:


df_cinsiyet.size().plot(kind="barh")


# In[23]:


sns.barplot(y=df["isim"][:10],x=df["servet"][:10])


# In[24]:


len(df["ülke"].unique())


# In[25]:


df_ülke= df.groupby("ülke")


# In[26]:


df_ülke_sayı= pd.DataFrame(df_ülke.size().sort_values(ascending=False), columns=["sayı"])


# In[27]:


df_ülke_sayı.head()


# In[28]:


sns.barplot(y=df_ülke_sayı["sayı"][:10],x=df_ülke_sayı.index[:10])


# In[29]:


df_türkiye = df[df["ülke"]== "Turkey"]


# In[30]:


df_türkiye["isim"].count()


# In[31]:


df_türkiye.head(10)


# In[32]:


sns.barplot(y=df_türkiye["isim"][:10], x =df_türkiye["servet"][:10])


# In[35]:


df["kategori"].unique()
#bu çıktıda boşlukları kaldırmak ve & işareti terine _ koymak için apply metodu kullanacağız.


# In[40]:


df["kategori"]=df["kategori"].apply(lambda x:x.replace(" ","")).apply(lambda x:x.replace("&","_"))
  


# In[43]:


df["kategori"].unique()


# In[44]:


df_kategori=df.groupby("kategori").size()


# In[45]:


df_kategori.plot()


# In[55]:


df_kategori=df_kategori.to_frame()
df_kategori.head()


# In[62]:


df_kategori = df_kategori.rename(columns={0:"sayı"}).sort_values(by = "sayı",ascending=False)
df_kategori.head()


# In[65]:


sns.barplot(x = df_kategori["sayı"][:10], y = df_kategori.index[:10])


# In[67]:


sns.scatterplot(x = df["yaş"], y= df["servet"])
#ilişki yoktur.


# In[69]:


sns.histplot(df["yaş"])


# In[73]:


df_yas = df.sort_values(by = "yaş")
df_yas.head()


# In[77]:


sns.barplot(y = df_yas["isim"][:10], x = df_yas.index[:10])


# In[ ]:




