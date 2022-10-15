#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


def url_casual_robe():
    url_casual = 'https://fr.shein.com/Women-Clothing-c-2030.html?attr_values=Casual&ici=fr_tab01navbar03&scici=navbar_WomenHomePage~~tab01navbar03~~3~~real_2030~~~~0&src_module=topcat&src_tab_page_id=page_home1665756357043&src_identifier=fc%3DWomen%60sc%3DV%C3%8ATEMENTS%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar03%60jc%3Dreal_2030&srctype=category&userpath=category-V%C3%8ATEMENTS&attr_ids=101_167&child_cat_id=1727'
    r = requests.get(url_casual)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('img'):
        print(link.get("data-src"))
        
url_casual_robe()
