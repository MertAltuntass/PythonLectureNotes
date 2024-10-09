#!/usr/bin/env python
# coding: utf-8

# In[2]:


def divide(number):
    return number / 2 


# In[4]:


divide(10)


# my_list = [1,2,3,4,5,6,7,8]

# In[10]:


for num in my_list:
    print(divide(num))


# ## Map

# In[13]:


list(map(divide,my_list))


# In[15]:


def control_string(string):
    if "Mert" in string:
        return True


# In[17]:


control_string("Mert")


# In[21]:


def control_string(string):
    return "Mert" in string
         


# In[23]:


control_string("Mert")


# In[25]:


my_artist_list = ["Mert","Martin","Queen"]


# In[27]:


list(map(control_string,my_artist_list))


# ## Filter

# In[30]:


list(filter(control_string,my_artist_list))


# ## Lambda

# In[33]:


def multi(number):  
    return number *3 


# In[35]:


multi(5)


# In[37]:


##def sumi(number): return sumi + 3 ## sadece 1 kere kullanıcam her yerde çağırmayacağım zaman kullanabilirim ve bu gösterimler böyle tek satırda yazılıyor.


# In[39]:


sumi = lambda number:number + 3


# In[41]:


sumi(3)


# In[ ]:




