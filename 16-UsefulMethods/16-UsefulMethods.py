#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list = [1,2,3,4,5,6,7]


# In[4]:


for number in my_list:
    print(number)


# In[6]:


##daha verimli oluşturulmak istediğimiz anlar kalabilir.


# In[8]:


##built-in kendiliğinden gelen method demek


# ## Range

# In[11]:


range(20)


# In[13]:


list(range(20))


# In[15]:


for number in list(range(20)):
    print(number * 5)


# In[17]:


for num in list (range(4,20)):
    print(num)


# In[19]:


for num in list(range(5,21,4)):
    print(num)


# ## Enumerate

# In[28]:


index = 0
for num in list(range(5,15)):
    print(f"no: {num} ix: {index}")
    index +=1


# In[31]:


for item in enumerate (list(range(5,15))):
    print(item)


# In[33]:


for (index,number) in enumerate(list(range(5,15))):
    print(index)
    print(number)


# ## Random

# In[38]:


from random import randint ## random'un randint diye bir kütüphanesini buraya koydu.


# In[40]:


randint(0,1000)


# In[42]:


randint(0,1000)


# In[44]:


my_list_2 = list(range(0,10))


# In[46]:


my_list_2


# In[54]:


from random import shuffle ##karıştır


# In[50]:


shuffle(my_list_2)


# In[52]:


my_list_2


# ## Zip

# In[57]:


## elimizde bir çok liste var ve bunları birleştirmek istiyoruz;


# In[59]:


sport_list = ["run","swim","basketball"]


# In[61]:


calories_list = [100,200,300]


# In[63]:


day_list = ["monday","tuesday","wednesday"]


# In[65]:


zip(sport_list,calories_list,day_list)


# In[67]:


new_list = zip(sport_list,calories_list,day_list)


# In[69]:


new_list


# In[71]:


new_list = list(zip(sport_list,calories_list,day_list))


# In[73]:


new_list


# In[75]:


for element in new_list:
    print(element)


# ## List Advanced

# In[84]:


new_list= []
my_string = "martin garrix"

for element in my_string:
    new_list.append(element)


# In[86]:


new_list


# In[92]:


new_list = [element for element in my_string] ##append ettiğim için bu şekilde kullanabiliyoruz.


# In[90]:


new_list


# In[94]:


new_list_2 = [number for number in list(range(0,10))]


# In[96]:


new_list_2


# In[ ]:




