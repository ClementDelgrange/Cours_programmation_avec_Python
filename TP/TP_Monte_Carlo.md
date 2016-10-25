% TP Monte Carlo
% Division des enseignements en informatique
% novembre 2016


Au cours de ce TP, nous cherchons à estimer la valeur de Pi en s'appuyant sur la méthode de Monte Carlo.

**Idée générale de la méthode :** en plaçant des points aléatoirement dans un domaine d'aire connue, lorsque le nombre de points tend vers l'infini, la proportion de points tombés dans un sous-domaine permet de déterminer son aire. 

$$
aire\_sous\_domaine = \frac{nb\_points\_dans\_sous\_domaine}{nb\_points\_total} * aire\_domaine
$$

Cela nécessite :

* de pouvoir tirer des points aléatoirement;
* de pouvoir compter ceux ayant attérit dans le sous domaine.

**Solution étudiée :**
Dans un repère orthonormé :

* l'aire du carré de côté 1 vaut 1;
* le quart de cercle de coté 1 inclu dans ce carré a pour aire Pi / 4.



1. Ecrivez une fonction de tirage alétoire de points dans un rectangle. Par défaut, si les coordonnées du rectangle ne sont pas renseignées, elles devront avoir pour valeur xmin=0, xmax=1, ymin=0 et ymax=1.
2. Testez votre fonction en tirant plusieurs points dans un le carré d'origine (0,0) et de côté 1.
3. Quelle condition permet de déterminer si un point (x,y) est à l'intérieur du du cercle de centre (x0,y0) et de rayon r ?
4. Ecrivez une fonction `est_dans_cercle(x, y, x0, y0, r)` retournant le booléen `True` si le point (x,y) est dans le cercle de centre (x0,y0) et de rayon r, et `False` sinon.
5. Ajoutez les valeurs par defaut suivante à votre fonction : `x0=0`, `y0=0` et `r=1`
6. Pour revenir à notre problème d'estimation de Pi, prévoyez une fonction `nb_dans_sous_domaine(n)` tirant n points aléatoires dans un carré de côté 1 et retournant le nombre de points à l'intérieur du quart de cerle de rayon 1 centré sur un coin du carré.
7. Utilisez votre dernière fonction pour estimer Pi en tirant 10, 100, 1000, ... 10000000 points.
8. Quels sont selon vous les points forts / points faibles de la méthode ?

Si vous avez terminé les questions précédentes, essayez de représenter graphiquement les tirages de points aléatoires à l'aide de la librairie `matplotlib`.

![Estimation de Pi à l'aide de la méthode de Monte Carlo](img/tp/monte_carlo.png)

Les instructions suivantes pourront être utiles :

* `import numpy as np` et `import matplotlib.pyplot as plt` pour importer les modules numpy et matplotlib
* `plt.plot(x, y, 'rx')` pour afficher une croix rouge sous le point (x, y)
* `plt.show()` pour afficher un graphique matplotlib
* `np.linspace(bi, bf, n)` pour découper un intervalle [bi, bf] en n éléments de même taille
