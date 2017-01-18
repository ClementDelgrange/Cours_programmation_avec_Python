% TP généralisation cartographique
% Division des enseignements en informatique
% novembre 2016


# Algorithme de Douglas-Peucker #
L'algorithme de Douglas-Peucker est utilisé pour simplifier une polyligne, en supprimant des points non significatif de la forme globale de la géométrie.

La simplification proposée consiste à remplacer une polyligne de plusieurs points par une ligne à deux points si la distance du point le plus éloigné de la droite formée par les extrémités de la polyligne est inférieure à un seuil.

![Principe de simplification d'une polyligne](img/tp/douglas_peucker-0.png)

Le principe de l'algorithme est le suivant : à l'étape initiale, les extrémités de la polylignes sont sélectionnées. Pour chacun des points entre ces deux extrémités, on calcule alors la distance du point à la droite liant les extrémités. La suite du traitement dépend de la valeur de la distance maximale ainsi calculée :

1. s'il n'y a aucun point, l'algorithme se termine (la ligne n'est pas simplifiable);
2. si la distance maximale est inférieure à un seuil donné, on supprime tous les points (ils sont non significatifs);
3. si la distance maximale est supérieure au seuil, la ligne n'est pas simplifiable : 
	* on divise la polyligne en deux parties allant de la première extrémité au point intermédiaire le plus distant et du point intermédiaire le plus distant à la deuxième extrémité;
	* on répète l'opération sur les deux parties.

![Principe de l'algorithme de Douglas-Peuker - source Wikipedia](img/tp/douglas_peucker.png)

\vspace{2em}

Dans tout ce qui suit, un point sera représenté par un couple de coordonnées `(x,y)`. Une droite ou un segment le sera par un couple de couples de coordonnées : `((x_a, y_a),(x_b, y_b))`.

Nous commencerons par écrire des fonctions générales qui nous seront utiles pour l'écriture de l'algorithme en question 4.

1. Ecrivez une fonction calculant la pente d'une droite. 
2. Ecrivez également une fonction calculant l'ordonné à l'origine d'une droite. Cette fonction prendra en paramètre les coordonnées d'un point A de la droite ainsi que sa pente.
3. Ajoutez une fonction `distance(point, droite)` effectuant le calcul de la distance d'un point A à une droite. Vous veillerez à traiter correctement les cas de droites verticales ou horizontales. Dans le cas général, la distance d'un point A à une droite d'équation $y = p.x + m$ sera données par la formule :

$$d = \frac{ \vert p*x_A - y_A + m \vert }{\sqrt{1 + p^2}}$$

4. Ecrivez une fonction `douglas_peuker(points, e)` simplifiant une liste de points selon la méthode de Douglas-Peucker avec un seuil e.
5. Testez différent seuils sur la liste de points suivants : `[(0,0), (1,0), (10,1), (11,1), (15,2), (17,1), (20,1), (27,0), (28,4), (30,6), (33,8), (34,0)]`

