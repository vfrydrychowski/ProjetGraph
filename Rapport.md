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

## Epinions

### Analyse descriptive

Dans cette analyse descriptive, nous allons examiner plusieurs propriétés du graphe d'un réseau social. Ce graphe représente une partie du réseau social Epinions qui est composé de sous-réseaux :

1. Les ratings (les notes données par les utilisateurs)
2. Les trusts (le niveau de confiance entre les utilisateurs)

Voici un tableau récapitulatif des propriétés du graphe d'Epinions :

<center>

| Metrique                        | Rating  |  Trust  |
| :------------------------------ | :-----: | :-----: |
| Nombre de noeuds                | 139738  |  49288  |
| Nombre de liens                 | 664825  | 487183  |
| in-degree min                   |    1    |    1    |
| out-degree min                  |    0    |    0    |
| in-degree max                   |  2026   |  2589   |
| out-degree max                  |  1023   |  1760   |
| in-degree median                |    1    |    2    |
| out-degree median               |    0    |    1    |
| in/out-degree moyen             |  4.76   |  9.88   |
| ecart type in-degree            |  20.02  |  20.02  |
| ecart type out-degree           |  21.29  |  21.29  |
| densité                         | 0.00003 | 0.0002  |
| Coef de clustering moyen        | 0.0032  | 0.1808  |
| Nombre de triangles (3-cliques) |  99969  | 1928214 |
| degré clique max                |    6    |    6    |

</center>

Il est aussi interessant de regarder la distribution des degrés des noeuds. Voici un histogramme des degrés des noeuds pour les ratings et les trusts :
![distribution des degrés](./Images/Epinions_degree_distribution.png)
On peut remarquer que les powerlaws s'ajustent particulièrement bien nos données.

Création de 2 types de configuration :

-   Une configuration avec 80% Train et 20% Test
-   Une configuration avec 90% Train et 10% Test

Ces deux configurations possèdent des hyperparamètres se rapprochant des conditions de test du rapport scientifique SocRec.

Comment ça fonctionne ?

-   Initialiser une configuration
-   Split les données en fonction du test
-   Lancer un train

### Delicious
