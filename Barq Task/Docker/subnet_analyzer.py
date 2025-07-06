#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the excel file : 
df = pd.read_excel('ip_data.xlsx')
print(df)


# In[2]:


import ipaddress
# The subnet calculations : 
# Example for one row : 
ip_str = '192.168.1.24'
subnet_mask = '255.255.255.0'

# convert subnet mask to prefix length
net = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask}", strict=False)

print(f"CIDR: {net.with_prefixlen}")
print(f"Network address: {net.network_address}")
print(f"Broadcast address: {net.broadcast_address}")
print(f"Usable hosts: {net.num_addresses - 2}")


# In[3]:


# Apply to the whole dataframe : 

def analyze_subnet(row):
    ip_str = row['IP Address']
    subnet_mask = row['Subnet Mask']
    net = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask}", strict=False)
    return pd.Series({
        'CIDR': net.with_prefixlen,
        'Network': str(net.network_address),
        'Broadcast': str(net.broadcast_address),
        'UsableHosts': net.num_addresses - 2
    })

results = df.apply(analyze_subnet, axis=1)
df = pd.concat([df, results], axis=1)
print(df)


# In[4]:


# Group by subnet : 

subnet_counts = df.groupby('CIDR').size().reset_index(name='Count')
print(subnet_counts)


# In[5]:


# Export report : 

df.to_csv('subnet_report.csv', index=False)


# In[6]:


# Visualizing : 

import matplotlib.pyplot as plt

plt.bar(subnet_counts['CIDR'], subnet_counts['Count'])
plt.xticks(rotation=45)
plt.ylabel('Number of Hosts')
plt.title('Number of Hosts per Subnet')
plt.tight_layout()
plt.savefig('network_plot.png')
plt.show()


# In[ ]:




