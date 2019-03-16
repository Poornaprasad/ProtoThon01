#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import random
import os
k=0
for i in range(1,5):
    j=open(f"poorna{i}.csv", "x")
    a= [['#', 'NUM1','NUM2','NUM3','NUM4','NUM5']]
    while os.stat(f"poorna{i}.csv").st_size< 2048:
        a.append([k,random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101)])
        k=k+1
        with open(f"poorna{i}.csv", 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(a)


# In[ ]:





# In[ ]:




