# Mon-armoire-intelligent


Ce projet a pour but de creer une armoire intelligente pour choisir le vetement ideal à porter en fonction de la temperatue de la ville, des tendences et du style de vetement.

Plan du travail:

- Introduction 
- Choix de la meteo 
- Les tendences des vetements 
- Shein
-Application
- Conclusion



## Introduction



## Choix de la meteo


## les tendances







## Shein

Notre choix de site s'est porté sur le site de vente de vetement et accesoires Shein, où nous avons selectionnés le nom, le lien et le style des differents vetements qui se trouve dans le site. Nous nous sommes focalisé sur ces differentes hypothèses car elles nous semblaient les plus importantes. Ainsi, nous avons extrait plus de  240 noms de vetements differents,4styles(Casual,Bohème,Sexy,Elegent) et 6 types de vetements(Manteaux,vestes,pantalons,pull,tshirt).

Pour realiser notre objectif, nous nous sommes muni du language de programmation Python. En premier temps,nous avons  telecharger les differents packages necessaires à l'etude qui sont: 
-BeautifuSoup: bibliotheque d'analyse des documents HTML qui nous sert d'analyse de Shein.
-Requests: lecture des documents HTTP
-pandas: gestion,nettoyage,filtrage de la base de données

Ensuite, dans une fonction ,nous avons recuperer les liens url de shein. Une fois le lien recuperé, nous avons extrait les differents liens et noms de vetement grace à la library Beautifulsoup, que nous avons ensuite enregistré dans des differents fichiers excel. Ces fichiers regroupent donc les liens de vetements par type de vetements(Manteaux,Vestes,pulls,robes) et par style(casual,Boheme,sexy et elegent). Par exemple, pour le style casual,nous avons creer 5 fichiers(robe casual,pull casual,veste casual)dans lesquelles nous les avons enregistré dans un dossier casual. Et ceci pour les autre style de vetement comme Sexy,elegent et Boheme.
Une fois tous les liens recuperés, nous les avons rassemblé grace à une fonction que nous avons appelé "Application".


## Application












## Conclusion





















## Conclusion



