#!/usr/bin/env python
# coding: utf-8

# In[2]:


##genelde listelerde kullanılıyor.


# In[4]:


my_list = [1,2,3,4,5]


# In[6]:


##bu listenin içerisindeki her bir elemanı tek tek ele aldığımız ve bunlar için tek tek işlem yaptığımız arkadaşa for deniyor


# In[16]:


for number in my_list:##her bir eleman için benim ismimi print etti
    print("Mert ALTUNTAS")##number hiç kullanmadık


# In[18]:


for number in my_list:
    print(number)


# In[20]:


for item in my_list:
    new_number = item * 5
    print(new_number)


# In[30]:


for number in my_list: ## 2 bölündüğünde 0 olanları yazdır denildi ama ben 2 ile tam bölünenleri buldum hangi sayılar olduğunu bulmak için yukarı bakmak zorunda kaldım :D 
    cift = number % 2 ## doğrusu bir alt satırda
    print(cift)


# In[36]:


for number in my_list:
    if number % 2 == 0:
        print(number)


# In[38]:


my_str = "Mert ALTUNTAS"
for letter in my_str:
    print(letter)


# In[40]:


my_tuple = (1,2,3)


# In[42]:


for item in my_tuple:
    print(item *5 -10)


# In[44]:


my_new_list = [("a","b"),("c","d"),("e","f"),("g","h")]


# In[46]:


for element in my_new_list:
    print(element)


# In[48]:


for (x,y) in my_new_list:
    print((x,y))


# In[50]:


for (x,y) in my_new_list:
    print(x)


# In[ ]:




