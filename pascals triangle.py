#!/usr/bin/env python
# coding: utf-8

# In[16]:


a=int(input("Enter the no of rows: "))
x=1
k=2*a-1
for i in range(0,a):
    for j in range(0,k):
        print(end=" ")
    for j in range(0,i+1):
        if(i==0 or j==0):
            x=1
        else:
            x=int(x*(i-j+1)/j)
        print(x,end=" ")
    print()
    k=k-1


# In[17]:


a=-2
b=int(a)
print(b)


# In[ ]:




