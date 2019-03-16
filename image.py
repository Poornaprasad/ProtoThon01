#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
img=mpimg.imread ((r"C:\Users\admin\Desktop\LASER.jpg"))
plt.figure(figsize = (3,3))
imgplot = plt.imshow(img)
pic=plt.show()
print('Image Hight {}'.format(img.shape[0]))
print('Image Width {}'.format(img.shape[1]))
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray = gray(img)  

plt.figure( figsize = (3,3))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.show()


# In[ ]:




