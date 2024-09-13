#!/usr/bin/env python
# coding: utf-8

# In[6]:


if 3 > 2:
    print("mert")
    print("123")


# In[16]:


x = 3


# In[18]:


y = 4


# In[20]:


if x > y:
    print("x is greater")
else:
    print("y is greater")


# In[22]:


x = 4


# In[24]:


y = 4 


# In[30]:


if x > y:
    print("x is greater")
elif x==y:
    print("x is y")
else:
    print("y is greater")


# In[32]:


my_superhero = input("superhero: ")


# In[34]:


if my_superhero == "Batman":
    print("wow")
elif my_superhero == "Superman":
    print("wow2")
elif my_superhero =="Ironman":
    print("wow3")
else:
    print(":/")


# In[36]:


a = 10


# In[38]:


b = 15


# In[40]:


c = 20 


# In[48]:


if a > b or b < c:
    print("kkk")
elif a < b and b > c:
    print("aaa")
else:
    print("mmm")


# In[50]:


isDead = False


# In[56]:


if isDead == True:
    print("character is dead")
else:
    print("character is not dead")


# In[58]:


if isDead:  ##
    print("character is dead")
else:
    print("character is not dead")


# In[60]:


if not isDead:
    print("character is not dead")


# In[62]:


my_string = "hello world"


# In[64]:


if my_string == "hello world":
    print("equal")


# In[66]:


if "hello" in my_string:
    print("true")
else:
    print("false")


# In[68]:


my_list = [1,2,3,4,5]


# In[70]:


if 2 in my_list:
    print("true")
else:
    print("false")


# In[72]:


my_dic = {"k1":100, "k2":200, "k3":300}


# In[78]:


if 100 in my_dic.keys(): ## values aradığımız için false veriyor a
    print("true")
else:
    print("false")


# In[ ]:




