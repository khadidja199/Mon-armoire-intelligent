# My smart wardrobe

*** Architectures, modèles et langages de données - projet de groupe***

*Al Bakaoui Chayma, AmadoU Khadidja, Harutyunyan Mariam*

Plan du travail 

- Introduction 
- Objectif
- Libraries utilisées
- Récupération des données météorologiques
- Récupération des données sur Shein
- Création de la fonction globale
- Génération du POP-UP intelligent
- Conclusion, difficultées et ouverture

## Introduction

Nous ne pouvons le nier, il est toujours difficile de choisir la tenue idéale le matin. Quel style de vêtement ? Quel type de vétêments ? Pour quelle température ? Ceux sont pleins de facteurs qui entrent en jeu lors du processus de décision.

Nous sommes partiS de ce dilemme pour créer un programme qui nous propose LA tenue en fonction de notre style (casual, bohème, élegant etc), du type de vêtement (pantalon, robe, veste etc) et de la température du jour de notre ville. 

---

## Objectif

Par le Web Scrapping, nous avons automatisé notre outil, afin qu'il puisse vous fournir une expérience de décision des plus simple et efficace.

Le choix du site à scrapper repose essentiellement sur le renseignement du style des vetêments. En effet, tous les sites de vente en ligne ne nous informe pas sur le style de leur articles. Nous avons également choisi arbitrairement de cibler une clientèle féminine bien que la logique du code puisse être appliquée également à partir de la catégorie homme. Dans ce cas, l'```url``` à scrapper sera différent : il correspondra au lien renvoyant à la page de vetêments pour homme.

Nous avons choisi le site Shein.fr, une grande entreprise chinoise en plein essor de vente en ligne (et désormais sur point de vente). 

## Librairies utilisées

les libraires utilisées sont les suivantes : 
- ```requests``` : il s'agit du package qui permet d'envoyer Python faire une requête sur une page HTTP
- ```pandas``` : c'est la librairie qui va nous permettre de manipuler facilement les données à analyser
- ```BeautifulSoup``` : ce package va nous permettre l'analyse des documents HTML et XML et une extraction de données par web scrapping 
- ```tkinter``` : libraire utilisée afin de générer le pop-up intelligent
- ```json``` : ce package va nous permettre d'avoir un format très simple d'échange de données inspiré par la syntaxe des objets littéraux de JavaScript, d'utiliser ce système de notation avec python pour notamment "sérialiser" des objets python de type ```dict``` ou ```list```
- ```datetime``` : cette librairie va nous fournir des classes permettant de manipuler les dates et les heures
- ```os``` : utilisée d'effectuer des opérations courantes liées au système d'exploitation
- ```Pil``` : utilisée pour le traitement d'image
- ```io``` : utilisée afin de nous faciliter le traitement de variables de différents types
- ```numpy``` : cette librairie est dédiée au calcul scientifique 
- ```random``` : nous avons utilisée cette librairie afin de générer aléatoirement des tenues
- ```glob``` : ce module est entré en jeu afin de rechercher tout les chemins correspondant à un motif particulier

## Récupération des données météorologiques

Commençons tout d'abord par récupérer les données météorologiques de la ville souhaitée. Ainsi, à l'aide du code suivant, d'une API, et d'une fonction nommée ```temperature()```; nous avons réussi à récupérer les températures moyennes, minimales, maximales, le taux d'humidité et l'état du ciel. Dans le cadre de notre projet, nous avons décider de nous concentrer seulement sur la température moyenne.

```
#Recuperation de la température

import requests
import json
import pandas as pd
import datetime

def temperature(ville):


    #récupère le temps actuel 
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
    #url="http://api.openweathermap.org/data/2.5/weather?q=Londres,uk&APPID=beb97c1ce62559bba4e81e28de8be095"

    r_weather = requests.get(url_weather)
    data = r_weather.json()

    #temperature moyenne
    t = data['main']['temp']  
    t = t-273.15
    #taux d'humidité
    humidite = data['main']['humidity']
    print("Taux d'humidite de {}".format(humidite) + "%")
    
    if 80 < humidite < 100:
        print("Prenez un parapluie")
    
    return t
```


## Récupération des données sur Shein

Après avoir préalablement installé les packages nécessaires, vient l'étape de la récupération des données depuis le site Shein. Nous avons selectionnés le type de vêtement ainsi que le style afin de récupérer les liens correspondants. Nous nous sommes focalisé sur ces differents critères car ils nous semblaient les plus importants. Ainsi, nous avons pu extraire plus de  240 noms de vêtements différents, quatre styles (sasual, bohème, sexy, elegant) et sept types de vêtements (manteaux, vestes, pantalons, pull, tshirt, robe, jupe).

```

#Elegant
#Pantalon

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def url_elegant_pantalon():
    url_elegant_pantalon = 'https://fr.shein.com/Women-Clothing-c-2030.html?attr_values=Elegant&ici=fr_tab01navbar03&scici=navbar_WomenHomePage~~tab01navbar03~~3~~real_2030~~~~0&src_module=topcat&src_tab_page_id=page_real_class1665775257714&src_identifier=fc%3DWomen%60sc%3DV%C3%8ATEMENTS%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar03%60jc%3Dreal_2030&srctype=category&userpath=category-V%C3%8ATEMENTS&attr_ids=101_257&child_cat_id=1740'
    r = requests.get(url_elegant_pantalon)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('img'):
        if link.get("data-src"):
            print(link.get("data-src"))
        
url_elegant_pantalon()

```

Ce code est un exemple quand le type de vêtement est pantalon et le style est élegant. Grâce à ce dernier, on récupère les ```urls```des images pour ce style et ce type de vêtement. 

Après avoir fait cela pour tous nos styles et tous nos types, on enregistre nos ```urls``` dans un dossier sur notre système d'exploitation. 



## Création de la fonction globale

Une fois que nous avons les ```urls``` pour chacun de nos styles et chacun de nos types de vêtements enregistrés dans des fichiers sur le système d'exploitation, on passe à la partie la plus importante à savoir paramétrer notre programme. De ce fait et à l'aide du code ci-dessous, nous créeons un code qui récupère les informations correspondantes au style choisi par l'utilisateur. 

```

styles = ["casual", "elegant", "boheme", "sexy"] 
dict_style = {"casual":1, "elegant":2, "boheme":3, "sexy":4}

data_final = pd.DataFrame()
for style in styles:
    xlfiles = glob.glob(os.path.join(os.path.join(path, style), "*.xlsx"))
    for i, xlfile in enumerate(xlfiles, 1):
        data = pd.read_excel(xlfile)
        tag = dict_style[style] * 10+i
        list_tag = [tag for i in range (len(data))]
        data["target"] = list_tag
        frames = [data_final, data]
        data_final = pd.concat(frames)

```
Après avoir récupérer le style de vêtement, nous définissons quel type proposer à l'utilisateur en fonction de la température locale du jour et tout cela aléatoirement à l'aide d'une uniforme.

```

def get_clothes(temp, data, style):
    dict_type = {
        (0,5): 2,
        (5,15):7,
        (0,10): (3,4),
        (10,20): (6,3),
        (20,50): [5, (6,1)]
                }
    list_choix = []
    for temp_compare, value in dict_type.items():
        if temp >= temp_compare[0] and temp < temp_compare[1]:
            if temp > 20 :
                if random.uniform(0,1) < 0.5:
                    list_choix.append(value[0])
                else:
                    list_choix.append(value[1][0])
                    list_choix.append(value[1][1])
            else:
                if type(value) == int:
                    list_choix.append(value)
                else:
                    list_choix.append(value[0])
                    list_choix.append(value[1])
    
    tags = [style * 10 + choix for choix in list_choix]
    list_image = []
    for tag in tags:
        data_tag = data[data["target"] == tag]
        n_article = np.random.randint(0, len(data_tag))
        list_image.append(data_tag.iloc[n_article]["URLS"])

    return list_image
    
```

Cette partie de notre code nous fournit des ```urls``` qui correspondent à une tenue. Néanmoins, un ```url``` n'est pas si intutif que ça, à quoi correspond cette chaîne de caractères ? Cela obligerait l'utilisateur de prendre cet ```url```, de le copier sur une barre de recherche afin de faire la correspondance avec une image. C'est beaucoup de travail, n'est-ce pas ? 

Etant dans une logique de faciliter l'utilisation, nous avons décider de convertir à l'aide du code suivant nos ```urls``` directement en images.

```
#Convertir url image en image

from PIL import Image
from io import BytesIO

def get_image_from_url(url):
    reponse = requests.get('http:'+ url,stream = True)
    return Image.open( BytesIO(reponse.content))
    
```

## Génération du POP-UP intelligent

Arrivés à ce stade de notre travail, il ne nous reste plus qu'à générer un POP-UP intelligent. Ce dernier regroupera nos fonctions et proposera directement les tenues en format image. 

```

#Fonction globale pour le POPUP

def onclick():
    style = style_entre1.get()
    region = region_entre2.get()
    temp = temperature(region)
    print(temp)
    if style.lower() in styles:
        style_ = dict_style[style.lower()]
        print(style_)
        list_url = get_clothes(temp, data_final, style_)
        for url in list_url:
            get_image_from_url(url).show()
    else:
        messagebox.showinfo("style", "please choose style from : {}".format(styles))
        
```

Comme on peux le voir ci-dessus, nous demandons à l'utilisateur de renseigner le style de vêtement souhaité ainsi que la région dans laquelle il se trouve. 

## Difficultées et ouverture

1. Difficultés 

Dans le cadre de ce projet, nous avons été tout d'abord un peu beaucoup ambitieuses. L'idée initiale était de récupérer toutes les informations à savoir le style, le type, la taille et la prix. Malheureusement, le site Shein.fr nous bloquait l'accès, il nous était impossible de récuperer n'importe quelle données et de ce fait des informations. Nous avons seulement réussi à récupérer les ```urls``` des images et nous avons en conséquence adapté notre projet à cette contrainte. 

Une autre difficulté ou plutôt limite du ```smart wardrobe``` et l'importance du nombre de données. Comme vous avez pu le constater, nous avons choisi arbitrairement de se concentrer sur un échantillon de style et de type puisque dans le cas contraire, nous aurions un nombre conséquent de données à manipuler. 


2. Ouverture

Ce projet peut faire l'objet d'une ouverture intéressante. En effet, nous pourrions l'étendre au domaine du machine learning. L'idée serait de :

- convertir les ```urls``` des images en vecteurs
- labelliser nos images par type et par style
- à l'aide du réseau neuronal convolutif, classifier nos images

Tout cela dans le but de créer un algorithme qui serai de quel type et de quel style appartient une nouvelle image qui n'est pas préenregistrer dans sa base de données. 

**Merci !**





