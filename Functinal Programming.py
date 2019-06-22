#!/usr/bin/env python
# coding: utf-8

# In[14]:


def naturalnumbers(n):
    cnt=1
    while(cnt <= n):
        print(cnt,end="  ")
        cnt=cnt+1
    print()
naturalnumbers(10)


# In[16]:


def factorial(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact
print(factorial(5))


# In[2]:


def palindromes(n1,n2):
    cnt=0
    while(n1<=n2):
        t=n1
        s=0
        while(t>0):
          r=t%10
          s=s*10+r
          t=t//10
        if s==n1:
          cnt=cnt+1
        n1=n1+1
    return cnt
print(palindromes(10,30))
print(palindromes(1,100))


# ## count of palindromes between two limits
