% TP Distance entre points
% Division des enseignements en informatique
% décembre 2016


Dans ce TP, nous cherchons à évaluer le dispersion de points tirés aléatoirement dans un carré de côté 1. Nous nous intéresserons aux distances minimale, maximale et moyenne entre les points, ainsi qu'à la position du centre de gravité du semi de points.

Tout au long du TP, un pont sera représenté par un couple de coordonnées `(x, y)`.

1. Ecrivez une fonction de tirage aléatoire d'un point dans une emprise définie par les coordonnées `((xmin, ymin), (xmax, ymax))`.
2. Ecrivez une fonction de tirage de n points aléatoires dans une emprise `((xmin, ymin), (xmax, ymax))`.
3. Modifiez votre fonction précédente pour que, si les coordonnées de l'emprise ne sont pas précisées, elles soient égales à `((0, 0), (1, 1))`
4. Complétez votre programme avec une fonction calculant le centre de gravité d'un ensemble de points (ie. la position moyenne des points).
5. Ajoutez une fonction calculant les distances minimale, maximale et moyenne d'un ensemble de points.
6. Observez comment évoluent ces valeurs lorsque le nombre de points du demi augmente.

