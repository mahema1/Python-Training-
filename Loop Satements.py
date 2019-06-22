#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=1
while(n<=10):
    print(n)
    n=n+1


# In[37]:


x=10
while(x>=1):
    print(x)
    x=x-1


# In[5]:


x=-22
while(x>=-45):
    print(x)
    x=x-1


# In[ ]:


x=1
sum=0
while(x<=10):
    sum=sum+x
    x=x+1
print(sum)


# In[36]:


x=int(input("Enter lower limit"))
y=int(input("Enter higher limit"))
sum=0
while(x<=y):
    if(x%2==0):
        sum=sum+x;
    x=x+1
print(sum)


# ## sum of even numbers

# In[39]:


x=int(input("Enter the number"))
while(x!=0):
    r=x%10
    print(r)
    x=x//10
    


# ## input: number
# ## output : extract the digits from right side

# In[44]:


x=int(input("Enter the number"))
sum=0
while(x!=0):
    r=x%10
    if(r%2==0):
        sum=sum+r
    x=x//10
print(sum)


# ## sum of even digits in a given number

# In[49]:


x=int(input("Enter the number"))
while(x!=0):
    r=x%10
    if(r==0):
        print("zero")
    elif(r==1):
        print("one")
    elif(r==2):
        print("two")
    elif(r==3):
        print("three")
    elif(r==4):
        print("four")
    elif(r==5):
        print("five")
    elif(r==6):
        print("six")
    elif(r==7):
        print("seven")
    elif(r==8):
        print("eight")
    elif(r==9):
        print("nine")
    x=x//10


# ## respective name to the digit

# In[ ]:


x=int(input("Enter the digit"))
y=int(input("Enter the number"))
z=int(input("Enter the number"))
count=0
x=int(input("Enter the number"))
while(x!=0):
    r=x%10
    if(r==x):
        count=count+1
    x=x//10


# ## input 3 numbers
# ## output how many times the digit is repeated between 2nd and 3rd number

# In[ ]:




