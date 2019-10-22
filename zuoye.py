#!/usr/bin/env python
# coding: utf-8

# In[1]:


m = []
for i in range(100):
    if i <2:
        continue
    for j in range(2,i):
        if i % j ==0:
                break
    else:
          m.append(i)
print(m)


# In[ ]:




