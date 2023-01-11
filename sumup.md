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

### PB

On veut prédire des rating manquant en propageant les rating des users dont on fait confiance.

