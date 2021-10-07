#!/usr/bin/env python
# coding: utf-8

# In[3]:


interface = input("management1 or not ? ")

if interface == "management1":
    print ("It is the management interface")

if interface != "management1":
    print ("It is NOT the management interface")


# In[6]:


max_interfaces = int(input("enter max_interfaces" ))

n = int(input("enter the interface number " ))

if n <= max_interfaces:
    print ("Interface number is within the range")
else:
    print ("Interface number is not within the range")


# In[7]:



device_list = ["10.10.10.11"]
if not device_list:
    print ("Empty List")
else:
    print ("Not Empty")


# In[9]:


device_list = ["10.10.10.11", "10.10.10.12", "10.10.10.13"]

for each_ip in device_list:
    print (each_ip)


# In[ ]:




