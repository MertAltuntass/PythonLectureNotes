#!/usr/bin/env python
# coding: utf-8

# In[2]:


##bir koşul tuttuğu sürece işlem yapmaya devam ediyor


# In[4]:


a = 0 


# In[6]:


while a < 5:
    print("hello")##burda sonsuz döngüye giricek o yüzden değerini artırıyorum.
    a = a + 1 


# In[8]:


my_list = [1,2,3,4,5]


# In[12]:


my_list.pop()


# In[14]:


my_list


# In[18]:


my_list.append(5)


# In[20]:


my_list


# In[22]:


while 4 in my_list:
    print("4 in my list")
    my_list.pop()
    


# In[51]:


number = 0


# In[53]:


while number < 10:
    if number == 5:
        break
    print(number)
    number += 1 # number = number +1 yazmak yerine bunu yazıyoruz.


# In[75]:


m = 0


# In[77]:


while m < 20:
    #print("value p: " + str(p))
    print(f"value m: {m}") ##f koyduktan sonra herhangi bir değişkeni bir string olarak yazdırabiliyoruz f""
    m += 1


# In[ ]:




