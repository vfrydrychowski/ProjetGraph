# Sum Up

## Intro

### trust relation <> social friendship

1. 2 users n'ont pas besoin de se faire confiance mutuellment pour avoir trust relation.

2. trust aware : users ont des goûts similaires.
Social aware : les goûts peuvent être différent.

3. Plus d'interaction social sur le WEB plutôt que de confiance.

Le but du papier est d'améliorer les algos de recommendations tradi sur ces 3 points.

## related work

### Collaborative filtering

+ *neighborhood based* : trouver des users ou items simiaires. Pearson Correlation Coefficient (PCC) Vector Space Similarity (VSS)
+ *model based* : model trained to predict users ratings on items. Not manipulating original datas. Clusturing, aspect model, latent factor, bayesian hierarchical, ranking.
Très efficaces : Low-rank matrix factorisation minimise MSE (SVD EM).

### Trust-Aware

Utilise un factueur de confiance dans les mesures de similarités pour propager les ratings. Aide à la coverage sans résuire l'accuracy.
Meilleur : fusion user/item avec user/user trust par latent user feature matrix.

## PB

On veut prédire des rating manquant en propageant les rating des users dont on fait confiance.

## Low-rank matrix factorization

On approxime la matrice de rating R(m*n) par une multiplication de 2 matrices :

+ U(m*l) : matrice des users sur l'espace l
+ V(n*l) : matrice des objets sur l'espace n
l est l'espace réduit pour optimiser les dimensions de R.

## Social Regularisation

### Model 1

On reprend l'équation 4 de la low rank matrix factorisation
On introduit la similarité entre entre un user et ses amis, pondéré par $\alpha$.
La similarité entre les amis est la valeur de U de l'ami par sa similarité normalisé par la similarité avec tout ses amis.

On fait une descente de gradien pour trouver U et V.

### Model 2

Problème du model 1: nos amis peuvent avoir des goûts très different de nous.

On essaie de prendre plus en compte les gens qui sont similaire à nous, la distance entre 2 users est moins importante si ils se resemblent moins.
