#!/usr/bin/env python
# coding: utf-8

# In[16]:


try:
    a=float(input("enter the first number: "))
    b=float(input("enter the second number: "))
    print("Please Enter the number for operation:\n1.Add\n2.sub\n3.Multiply\n4.Division")
    c=int(input())
    operation={"1":a+b ,"2":a-b,"3":a*b,"4":a/b}
    if c==1:
        p=operation["1"]
        print(f"The sum is{p}")
    elif c==2:
        q=operation["2"]
        print(f"The Difference is{q}")
    elif c==3:
        r=operation["3"]
        print(f"The product is{r}")
    elif c==4 and b!=0:
        s=operation["4"]
    elif c==4 and b==0:       
        print("Zero Division Error")
except:
    print("ERROR")
    


  




    


# In[ ]:





# In[ ]:





# In[ ]:




