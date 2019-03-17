#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


import imaplib
def read():

    userName = "xxxx@gmail.com"
    password = "xxxx" 
    email_ids = [userName]
    imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
    imap_server.login(userName, password)
    imap_server.select('INBOX')
    status, response = imap_server.status('INBOX', "(UNSEEN)")
    print(stat)
    print(response)
read()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




