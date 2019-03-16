#!/usr/bin/env python
# coding: utf-8

# In[11]:


import itertools as it
from PyDictionary import PyDictionary
a=[]
for i in it.permutations("protosem"):
    a.append("".join(i))
'''count=0
for i in a:
    if i in Dictionary:
        count=count+1
print(count)'''


# In[ ]:




