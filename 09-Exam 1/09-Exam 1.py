#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.


# In[4]:


my_string = "James Hetfield"


# In[6]:


# Cevap 1)


# In[213]:


my_letter= my_string[4]


# In[215]:


my_letter


# In[18]:


# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)


# In[20]:


my_new_string = "QuentinTarantino"


# In[22]:


# Cevap 2)


# In[219]:


my_new_string[4:8]


# In[26]:


# Aşağıdaki String'i kod ile tersten yazın


# In[28]:


my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"


# In[30]:


# Cevap 3)


# In[54]:


my_last_string[::-1]


# Integer & Float

# In[57]:


# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?


# In[59]:


3 + 10.2 + 50


# In[61]:


# Cevap 1)


# In[63]:


x = 3 + 10.2 + 50


# In[65]:


type(x)


# In[67]:


# 2) Aşağıdaki işlemin sonucu kaçtır?


# In[69]:


x = 5 + 8 * 12


# In[71]:


x


# List & Dictionary & Set

# In[74]:


# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"] burayı yanlış anladığım için yanlışımıda bırakıyorum ve doğrusunu ekliyorum.


# In[76]:


# Cevap 1.a)


# In[78]:


my_list= [1,2,"a"]


# In[80]:


my_list


# In[82]:


# Cevap 1.b)


# In[84]:


my_dic={1,2,"a"}


# In[86]:


my_dic


# In[88]:


# Cevap 1.c)


# In[90]:


my_set = [1,2,"a"]


# In[92]:


my_set


# In[ ]:


##doğrusu


# In[223]:


my_list_1 = [1,2,"a"]


# In[225]:


my_list_2 = []


# In[227]:


my_list_2.append(1)


# In[229]:


my_list_2.append(2)


# In[231]:


my_list_2.append("a")


# In[233]:


my_list_2


# In[235]:


my_list_3 = list()


# In[237]:


my_list_3.append(1)


# In[239]:


my_list_3.append(2)


# In[241]:


my_list_3.append("a")


# In[243]:


my_list_3


# In[94]:


# 2) Aşağıdaki "a"'yı tek satırda alınız:


# In[96]:


my_list = [1,4,[2,3,"a"]]


# In[130]:


my_list[2][2]


# In[132]:


# 3) Aşağıdaki "b"'yi tek satırda alınız:


# In[247]:


my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]} ##buna bakayım


# In[251]:


my_dictionary["kk"][1]["kkkk"]


# In[178]:


# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?


# In[184]:


my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45] #set olunca 1'den fazla değerleri kabul etmiyor bu yüzden 1 adet olanlar kalacaktır.


# In[194]:


my_list_to_be_set


# Boolean

# In[197]:


# 1) Aşağıdaki ifadenin sonucu ne olacaktır?


# In[199]:


x = 40 * 5 + 3


# In[201]:


y = 208 - 2 * 4


# In[203]:


x > y


# In[205]:


# 2) Aşağıdaki ifadenin sonucu ne olacaktır?


# In[207]:


a = 40 * (4 - 2)


# In[209]:


b = 80 - 2 * -5


# In[211]:


a > b


# In[ ]:




