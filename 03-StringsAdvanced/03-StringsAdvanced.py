#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string = "Mert ALTUNTAS"


# In[3]:


my_string


# ##indexing

# In[6]:


my_string[0]


# In[8]:


my_string[3]


# In[10]:


my_string[-1]


# In[12]:


my_string[-2]


# In[14]:


my_string_2 = "1234567890"


# In[16]:


my_string_2[0]


# In[18]:


my_string_2[2:]


# #Slicing

# In[23]:


my_string_2[4:]


# In[25]:


my_string_2[:2]


# ##stopping index

# In[28]:


my_string_2[:4]


# In[30]:


my_string_2[2:4]


# In[32]:


my_string_2[5:8]


# ##step size

# In[35]:


my_string_2[::]


# In[37]:


my_string_2[::3]


# In[41]:


my_string_2[::2]


# In[43]:


my_string_2[2:4:2] ##2 başla 4 dur 2şer atla


# In[47]:


my_string_2[::-1] ##tersine çevirmiş oluyoruz


# ##String Methods

# In[9]:


my_name = "mert"


# In[15]:


my_name_capitalized=my_name.capitalize()


# In[13]:


my_name


# In[17]:


my_name_capitalized


# In[19]:


my_name = "Mert ALTUNTAŞ"


# In[21]:


my_name.split()


# In[25]:


my_name_split=my_name.split()


# In[27]:


my_name_split


# In[29]:


my_number = 123


# In[31]:


my_name.upper()


# In[35]:


"mert" *10 ##python buna izin veriyor ama float değerlere izin vermiyor o kadar da değil diyor :D 


# In[37]:


"mert" + "5"


# In[39]:


my_name = "Mert"


# In[41]:


my_surname="ALTUNTAS"


# In[47]:


my_full_name=my_name+" "+ my_surname


# In[49]:


my_full_name


# In[ ]:




