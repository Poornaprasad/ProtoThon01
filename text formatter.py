#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Enter the Sentence")
a=input()
n=len(a)
print("1.all caps")
print("2.small caps")
print("3.title case ")
print("4.start case")
choice=int(input("type 1/2/3/4: "));
if(choice==1):
    print(a.upper())
if(choice==2):
    print(a.lower())
if(choice==3):
    print(a.title())
if(choice==4):
    print(a[0].upper(),end='')
    print(a[1::])


# In[ ]:




