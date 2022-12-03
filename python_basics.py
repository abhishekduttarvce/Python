#!/usr/bin/env python
# coding: utf-8

# In[1]:


(711.25 - 235.14) * 75


# In[2]:


_*0.80


# In[3]:


help()


# In[6]:


abs(_)


# In[7]:


_* -1


# In[8]:


abs(_)


# In[9]:


round(_, 2)


# In[10]:


_*9


# In[11]:


_*9.99999


# In[12]:


round(_)


# In[13]:


round(_,4)


# In[14]:


_


# In[15]:


_ *9.999999


# In[16]:


round(_, 4)


# In[17]:


12 + 20


# In[18]:


(3 + 4
         + 5 + 6)


# In[19]:


for i in range(5):
        print(i)


# In[21]:


i=1;
for i in range(5):
        print(i)


# In[22]:


for i in range(6):
        print(i)


# In[26]:


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
        print(pt.text)


# In[27]:


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for fd in doc.findall('.//fd'):
        print(fd.text)


# In[28]:


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for anyname in doc.findall('.//fd'):
        print(anyname.text)


# In[29]:


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for anyname in doc.findall('.//scheduled'):
        print(anyname.text)


# In[30]:


print('hello world')


# In[ ]:




