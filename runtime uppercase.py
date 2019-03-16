#!/usr/bin/env python
# coding: utf-8

# In[2]:


import keyboard
import time
a="abcdefghijklmnopqrstuvwxyz"
l=[]
for i in a:
    l.append(i)
while True:
    time.sleep(0.2)
    try:
        for i in l:
            if keyboard.is_pressed(i):
                print(i.upper(),end="\r")
                continue
    except:
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import keyboard
i="a"
if keyboard.is_pressed(i):
    print(i.upper(),end="\r")


# In[1]:


import keyboard 
  
# It records all the keys until escape is pressed 
rk = keyboard.record(until ='Esc') 
  
# It replay back the all keys 
keyboard.play(rk, speed_factor = 1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




