#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_string = "Mert"


# In[4]:


my_string.upper()


# In[6]:


my_string


# In[8]:


my_string_upper = my_string.upper()


# In[10]:


my_string


# In[12]:


my_string_upper


# In[14]:


help(my_string.split)


# In[16]:


def helloworld():
    print("hello")
    print("World")
    


# In[18]:


helloworld()


# ## INPUT & RETURN

# In[21]:


def hello_programming(name):
    print("hello")
    print(name)


# In[23]:


hello_programming("python")


# In[25]:


hello_programming("Java")


# In[27]:


def hello_prg(name="Python"):
    print("hello")
    print(name)


# In[29]:


hello_prg()


# In[31]:


hello_prg("mert")


# In[40]:


def summ (number1, number2):
    number3= number1 + number2
    print(number3)


# In[42]:


summ(5,8)


# In[44]:


summ(10,-500)


# ## Return

# In[46]:


def summation(num1,num2,num3):
    return num1+num2+num3


# summation(10,20,30)

# In[52]:


my_result = summation(10,20,30)


# In[57]:


my_result


# In[59]:


my_integer = summ(10,20)


# In[61]:


my_integer


# In[63]:


type(my_integer)


# In[65]:


def control_string(s):
    if s[0] == "m":
        print("mmm")


# In[69]:


control_string("paris")


# In[71]:


control_string("mert")


# In[73]:


def control_string(s):
    if s[0] == "m":
        print(s.capitalize())


# In[75]:


control_string("mert")


# ## Arbitrary arguments & Key word arguments

# In[3]:


def summation_2(num1,num2):
    return num1 + num2


# In[5]:


# *args


# In[9]:


def sumx2(*args):
    return sum(args)


# In[11]:


sumx2(10,20,30)


# In[13]:


sumx2(10,20,30,40,50)


# In[21]:


def my_func(*args): ##arg olayı ben ne verirsem onu alıyor ama esas olay yıldız işaretinde.
    print(args)


# In[17]:


my_func(10,20)


# In[19]:


my_func("a","b",1,2)


# In[23]:


def my_func_2(*mert):
    print(mert)


# In[25]:


my_func_2(10,20,30)


# In[27]:


def example_func(**kwargs):
    print(kwargs)


# In[29]:


example_func(run=100,walk=50,swim=200)


# In[31]:


def keyword_func(**kwargs):
    if "Mert" in kwargs:
        print("Mert MErt")
    else:
        print(".......")


# In[35]:


keyword_func(Mert=10,Yrtx=20,ekksd=40)


# In[37]:


keyword_func(xae=10,sjda=40)


# In[ ]:




