# Rapport 

## Intro

### Pré-Traitement
Les données d'entrées pour les ratings sont de la forme suivante:
User_id Item_id Rating

Les données d'entrées pour les trusts sont de la forme suivante:
User_id User_id Boolean  
Le Boolean vaut 1 si l'utilisateur 1 trust l'utilisateur 2, 0 sinon
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