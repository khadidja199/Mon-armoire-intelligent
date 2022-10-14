#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

url = 'https://fr.shein.com/trends/New-in-Trends-sc-00654187.html?ici=fr_tab01navbar02&scici=navbar_WomenHomePage~~tab01navbar02~~2~~itemPicking_00654187~~~~0&src_module=topcat&src_tab_page_id=page_home1665673115546&src_identifier=fc%3DWomen%60sc%3DAUTOMNE-HIVER%202022%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar02%60jc%3DitemPicking_00654187&srctype=category&userpath=category-AUTOMNE-HIVER-2022'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for link in soup.find_all('img'):
    print(link.get("data-src"))
