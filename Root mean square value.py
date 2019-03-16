#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


ar = list(map(float, input().rstrip().split(",")))
sq=[]
for i in ar:
    sq.append(i**2)
a=sum(sq)
b=a/len(ar)
b=b**0.5
print(f"The RMS is {b}")


# In[2]:





# In[ ]:




