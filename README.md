# Projet Scraping Allocine
Le but du projet est de scraper les informations d'une série TV ainsi que les avis des spectateurs rattachés à cette série. Nous scrapons le site internet https://www.allocine.fr/.
Ces informations seront stockées dans des fichiers .json qui seront eux-mêmes stockées dans une base de données MongoDB.
Ces données seront utiliser afin d'effectuer de la data visualization. 

Une partie en NLP a été réalisée afin de vérifier si l'avis d'une série est positif ou négatif après l'analyse de ce dernier.

# Outils et technologies utilisées 

> - Python
> - Jupyter Notebook
> - MongoDB
> - NLP
> - Plotly, Pandas etc.. (plusieurs libs)

Nous souhaitions également utiliser les outils suivant:
> - Elasticsearch
> - Kibana
> - Docker


# Dossier
Chaque dossier correspond à une des trois parties du projet. 

**data-acquisition-allocine** : *La partie scraping*

**data-processing-allocine** : *La partie mongoDB et NLP*

**data-visualization-allocine** : *La partie data-visualisation*


Pour plus d'informations sur les scripts et notebook vous pouvez vous référez au rapport fourni à la racine du projet :octocat:. 