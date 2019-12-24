#!/usr/bin/env python
# coding: utf-8

# # python
# - Topics covered
#   - operators
#   - data types
#   - conditional statements

# # python
# - Topics covered
#   1. operators
#   2. data types
#   3. conditional statements

# *Python*
# **Python**
# ***python***

# In[1]:


print("hello world")


# In[2]:


print("pandu",end="@")
print("pandu")


# In[3]:


a=10
a*a


# In[4]:


name="GITAM"
address="hyd"
print(name,"universty","place",address)


# In[5]:


input("enter your name")


# In[6]:


b=int(input())
type(b)


# In[7]:


b=input()
type(b)


# In[8]:


x=11
y=12.5
z=x+y
print(type(x),type(y),type(z))


# In[10]:


c=complex(3,4)
print (c)


# In[11]:


v=complex(1,5)
print(v)


# In[12]:


i=100
print(type(i))
j=str(i)
print(type(j))
k=float(i)
print(type(k))


# In[14]:


a="100"
print(type(a))
b=float(a)
b


# In[15]:


x=12
y=17
x+y


# In[16]:


x=12
y=17
print(x+y)
print(x-y)
print(x/y)
print(x%y)
print(x*y)
print(x**y)


# In[18]:


a=12
b=17
print(a>=12 and a<=17)
print(a>=15 and a<=17)


# In[19]:


x=6
y=3
print(x>y)
print(x<y)
print(x!=y)
print(x==y)
print(x>=y)
print(x<=y)


# In[20]:


str1="mohit"
print('a' in str1)
print('o' in str1)


# In[22]:


a=23
b=200
if b>a:
 print("b is greater than a")


# In[23]:


a=23
b=23
if b>a:
    print("b is greater than a ")
else:
    print("a is greater than b")


# In[24]:


a=23
b=23
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
elif a>b:
    print("a is greater than b")


# In[ ]:


1 year =int(input("enter year:"))
# leap year check
if year%4==0 and year%100!=0:
    

