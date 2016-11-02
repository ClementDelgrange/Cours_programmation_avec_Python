% TP généralisation cartographique
% Division des enseignements en informatique
% novembre 2016


# Algorithme de Douglas-Peucker #
L'algorithme de Douglas-Peucker est utilisé pour simplifier une polyligne, en supprimant des points non significatif de la forme globale de la géométrie.

Le principe de la simplification est de remplacer une polyligne de plusieurs points par une ligne à deux points si la distance du point le plus éloigné de la droite formée par les extrémités de la polyligne est inférieure à un seuil.

L'algorithme met en oeuvre l'approche *diviser pour mieux régner*. A l'étape initiale, les extrémités de la polylignes sont sélectionnées. On parcours alors tous les points entre ces extrémités pour calculer la distance maximale entre ces points et la droite liant les deux extrémités :

1. s'il n'y a aucun point, l'algorithme se termine (la ligne n'est pas simplifiable);
2. si la distance est inférieure à un seuil donné, on supprime tous les points (ils sont non significatifs);
3. si la distance est supérieure au seuil, la ligne n'est pas simplifiable : 
	* on divise la polyligne en deux parties allant de la première extrémité au point le plus distant et du point le plus distant à la deuxième extrémité;
	* on répète l'opération sur les deux parties.

![Principe de l'algorithme de Douglas-Peuker - source Wikipedia](img/tp/douglas_peucker.png)

\vspace{2em}

Dans tout ce qui suit, un point sera représenté par un tuple de coordonnées (x,y). Une droite ou un segment le sera par un tuple de tuple ((x$_A$,y$_A$),(x$_B$,y$_B$)).

1. Ecrivez une fonction calculant la pente d'une droite (AB). 
2. Prévoyez également une fonction calculant l'ordonné à l'origine d'une droite (AB). Cette fonction prendra en paramètre les coordonnées des deux points A et B et la pente de la droite.
3. Ajoutez une fonction `distance(pointA, droite)` effectuant le calcul de la distance d'un point A à une droite. Vous prendrez soin de traiter les cas d'une droite verticale ou horizontale. Dans le cas général, la distance d'un point A à une droite d'équation $y = p.x + m$ sera données par la formule :

$$d = \frac{ \vert p*x_A - y_A + m \vert }{\sqrt(1 + p**2)}$$

4. Ecrivez une fonction `douglas_peuker(points, e)` simplifiant une liste de points selon la méthode de Douglas-Peucker avec un seuil e.
5. Testez différent seuils sur la liste de points suivants : `[(0,0), (1,0), (10,1), (11,1), (15,2), (17,1), (20,1), (27,0), (28,4), (30,6), (33,8), (34,0)]`

