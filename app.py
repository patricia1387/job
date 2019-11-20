#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open('input.csv', mode='w') as csv_file:
    fieldnames = ['name', 'animal', 'birthday_year']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'Bojko', 'animal': 'rabbit', 'birthday_year': '1999'})
    writer.writerow({'name': 'Kira', 'animal': 'dog', 'birthday_year': '2008'})
    writer.writerow({'name': 'Hryzko', 'animal': 'hamster', 'birthday_year': '2016'})
    writer.writerow({'name': 'Labka', 'animal': 'cat', 'birthday_year': '2014'})
    writer.writerow({'name': 'Ninja', 'animal': 'turtle', 'birthday_year': '1959'})
    writer.writerow({'name': 'Rex', 'animal': 'dog', 'birthday_year': '2009'})


# In[ ]:




