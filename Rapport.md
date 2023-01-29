# Rapport 

## Intro

### Pré-Traitement
Les données d'entrées pour les ratings sont de la forme suivante:  
| User_id | Item_id | Rating |
| :-----: |:------: | :----: |  

Les données d'entrées pour les trusts sont de la forme suivante:  
| User_id | User_id | Trust |
| :------:| :-----: | :---: | 

La variable Trust est un Booléen vaut 1 si l'utilisateur 1 trust l'utilisateur 2, 0 sinon
#### Epinions
Création de 2 types de configuration :
- Une configuration avec 80% Train et 20% Test
- Une configuration avec 90% Train et 10% Test  

Ces deux configurations possèdent des hyperparamètres se rapprochant des conditions de test du rapport scientifique SocRec.

Comment ça fonctionne ?
- Initialiser une configuration 
- Split les données en fonction du test
- Lancer un train 

### Delicious
- On a essayé de faire les mêmes fichier que pour épinions:  
  - Normalisation des ratings entre 1 et 5 
  - Rating basé sur le nombre de fois que le user à tag une url  et ça pour chaque user et pour chaque url
  - Pour les trust c'est juste s'ils sont en contact alors ils se trust 


## Extension du modèle 

- Deux mesures de similarité entre utilisateurs:
  - Mesures de similarités de noeuds dans un graphe (chapitre 1):
    Nous avons implémenté la similarité de Jaccard.

  - Mesure basée sur les notions développées  par  les  groupes  d’étudiants:  
    Nous avons implémenté la notion: Node2vec.  
    Dans Node2vec, nous traitons les nœuds d'un graphe comme des mots dans un corpus et utilisons Word2Vec pour apprendre leurs représentations. L'objectif est de capturer les relations structurelles entre les nœuds du graphe, telles que leur proximité et leur connectivité, dans un espace vectoriel de faible dimension. Cela nous permet de réaliser des tâches de prédiction de liens et donc proposer des récommendations.

- idée de groupe :  
    Nous avons mis en place la détection de communauté.  
    Pour se faire, nous avons créer le graphe de user (relations followers et follwees). Puis, nous avons utiliser l'algorithme de Louvain (extraction de communautés dans de grands réseaux). Ensuite, nous avons pris en compte les communautés dans la mesure de similarité. Pour être plus précis, dans l'algorithme de base la similarité se fait entre tous les followees d'un user. Or, nous nous sommes dit qu'il serait plus intéressant de prendre seulement les followees d'un user appartenant à la même communauté que ce dernier. 


## Expérimentation et analyse des résultats

Pricipalement pour Délicious:
- Jaccard same résult 
- Détection de commu same résult et c'est plus long
- Node2vec ?
- On arrive de base à avoir des résult quasi similaire mais pas tout à fait ce qui veut dire que soit on a pas le même code, soit on a pas les mêmes données soit ils ont pris le min résult et pas la moyenne soit ils ont cheat(pas sur) + on a pas tous les hyperparamètres dans l'article donc cela peut jouer

Conclu => on a fait un banger qui améliore les résult de 1.829 %