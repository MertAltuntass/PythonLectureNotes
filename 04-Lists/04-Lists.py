#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string = "Mert"


# In[3]:


my_string[0]


# In[5]:


my_string[1]


# In[10]:


#my_string[0] = "B"


# ##immutability

# In[12]:


#my_string[2] = "A"


# In[14]:


my_list= [1,2,3]


# In[16]:


my_list[0]


# ##mutable

# In[20]:


my_list


# In[18]:


my_list[0] = 5


# In[23]:


my_list.append(7)


# In[25]:


my_list


# In[35]:


my_string="sabre"


# In[29]:


my_string.capitalize()


# In[31]:


my_string


# In[33]:


my_list


# In[37]:


my_list.pop()


# In[39]:


my_list


# In[41]:


my_mixed_list=[1,2,"a","bwe"]


# In[43]:


my_mixed_list[0]


# In[45]:


my_mixed_list[-1]


# In[47]:


my_list_1 = ["a","b","c"]


# In[49]:


my_list_2 = ["d","e","f"]


# In[51]:


my_list_3 = my_list_1 + my_list_2


# In[53]:


my_list_3


# In[55]:


my_list_1 *3 


# In[57]:


my_list_1 +5 


# In[59]:


my_list_1 *5.3


# In[61]:


my_list_1.reverse()


# In[63]:


my_list_1


# ##nested list

# In[66]:


new_list = [1,4,"a"]


# In[68]:


new_list = [1,4,"a",[3,"c"]]


# In[70]:


new_list[3]


# In[72]:


nested_list = new_list[3]


# In[74]:


nested_list


# In[76]:


nested_list[1]


# In[78]:


new_list[3][1]


# In[80]:


new_list


# In[82]:


new_list[2:]


# In[84]:


new_list[:2]


# In[ ]:




