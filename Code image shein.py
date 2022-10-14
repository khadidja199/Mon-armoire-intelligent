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
        im = requests.get(link)
        f.write(im.content)
        print('Writing: ', name)

#imagedown('https://fr.shein.com/trends/New-in-Trends-sc-00654187.html?ici=fr_tab01navbar02&scici=navbar_WomenHomePage~~tab01navbar02~~2~~itemPicking_00654187~~~~0&src_module=topcat&src_tab_page_id=page_home1665673115546&src_identifier=fc%3DWomen%60sc%3DAUTOMNE-HIVER%202022%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar02%60jc%3DitemPicking_00654187&srctype=category&userpath=category-AUTOMNE-HIVER-2022', 'image_shein')


# In[ ]:





# In[2]:


r=requests.get(url)


# In[3]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[4]:


images = soup.find_all('img')


# In[5]:


images


# In[6]:


for image in images:
    link=soup.select("[scr]")


# In[7]:


results=soup.find_all('img')
results


# In[ ]:


for result in results:
    results.append(result)


# In[ ]:


#productsdf =  pd.DataFrame(results)


# In[ ]:


result.to_csv('liens.csv')


# In[ ]:





# In[ ]:





# In[ ]:


for image in images:
        name = soup.select("[alt]")
        link = soup.select("[scr]")
        #im = requests.get(link)


# In[16]:


import pandas as pd
nameStr = str(name)
nameStr.replace(' ', '-').replace('/', '') + '.png', 'wb'


# In[20]:


img = soup.select_one("[src]")
print(img["src"])


# In[52]:


for image in images:
    name = soup.select("[alt]")
    link = soup.select("[src]")
    print(name)


# In[ ]:


page = urllib.urlopen("https://en.wikipedia.org/wiki/Donald_Trump").read()
soup = BeautifulSoup(page, "html.parser")
nickname = soup.find_all("span", class_="nickname")
nicknameStr = str(nickname)
nicknameStr.replace('[<span class="nickname">','')
nicknameStr.replace('</span>]','')
print(nicknameStr)


# In[27]:


link = soup.select("[scr]")


# In[28]:


print(link)


# In[ ]:




