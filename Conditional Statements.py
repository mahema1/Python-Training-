#!/usr/bin/env python
# coding: utf-8

# #Control Statements

# In[3]:


x=10
if(x<15):
    print("the number is less than 15");


# In[6]:


x=10
if(x<15):
    print("hello")


# In[10]:


x=10
if(x>15):
    print("Good Morning")
else:
    print("Good Afternoon")


# In[15]:


x=2
y=4
if(x>y):
    print(x,"greater")
else:
    print(y,"greater")


# In[22]:


x=2
y=3
z=4
if(x>y and y>z):
    print(x,"is greater")
if(y>x and y>z):
    print(y,"is greater")
else:
    print(z,"is greater")


# In[24]:


x=2
y=4
if(x==y):
    print(x*x)
else:
    print(x*y)


# In[27]:


x=4
y=4
if(x==y):
    print(x*x)
else:
    print(x*y)


# In[29]:


x=1
if(x==0):
    print("Given number is zero")
elif(x>0):
    print("Given number is positive")
else:
    print("Given number is negaive")


# In[ ]:




