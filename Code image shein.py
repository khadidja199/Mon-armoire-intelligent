#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

url = 'https://fr.shein.com/trends/New-in-Trends-sc-00654187.html?ici=fr_tab01navbar02&scici=navbar_WomenHomePage~~tab01navbar02~~2~~itemPicking_00654187~~~~0&src_module=topcat&src_tab_page_id=page_home1665673115546&src_identifier=fc%3DWomen%60sc%3DAUTOMNE-HIVER%202022%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar02%60jc%3DitemPicking_00654187&srctype=category&userpath=category-AUTOMNE-HIVER-2022'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')

for image in images:
    name = soup.select("[alt]")
    link = soup.select("[scr]")
    linkStr=str(link)
    nameStr = str(name)
    with open(nameStr.replace('-', '').replace('/', '') + '.png', 'wb') as f:
        liens_image = requests.get(link)
        f.write(liens_image.content)
        print('Writing: ', name)

#imagedown('https://fr.shein.com/trends/New-in-Trends-sc-00654187.html?ici=fr_tab01navbar02&scici=navbar_WomenHomePage~~tab01navbar02~~2~~itemPicking_00654187~~~~0&src_module=topcat&src_tab_page_id=page_home1665673115546&src_identifier=fc%3DWomen%60sc%3DAUTOMNE-HIVER%202022%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar02%60jc%3DitemPicking_00654187&srctype=category&userpath=category-AUTOMNE-HIVER-2022', 'image_shein')
