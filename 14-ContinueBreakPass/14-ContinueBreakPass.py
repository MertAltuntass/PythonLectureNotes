#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list = [10,20,30,50,60]


# In[4]:


for number in my_list:
    print(number)


# In[6]:


for num in my_list:##eğer loop durdurmak istersem break.
    if num == 30:
        break
    print(num *5)


# In[8]:


for item in my_list: ##eğer loop bir sayıyı hesaba katmamak işlem yapmamak isteyip başa dönmek istersem bunu kullanıyorum.
    if item == 30:
        continue
    print(item *5)


# In[14]:


for sen in my_list:##pratik amaçla kullanılır, bir şey karar veremediğinizde pass kullanıyorsunuz böylece hata almıyorsunuz.
    pass ##hiç bir şey yapma yoluna devam et ama hatada verme.


# In[ ]:




