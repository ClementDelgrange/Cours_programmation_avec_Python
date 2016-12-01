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



3) On suppose que chaque point p i représente un foyer d’habitation. Le semis représente une ville dans
laquelle on souhaite déterminer l’emplacement d’un bureau de vote de sorte à minimiser la somme des
déplacements de ses habitants. Autrement dit, on recherche la position de la médiane géométrique :
n
||p i − p|| 2
P = argmin
p∈R 2
i=1
Ecrire un algorithme itératif (i.e. partant d’une position initiale aléatoire et améliorant itérativement sa
qualité jusqu’à convergence) pour déterminer les coordonnées de P .

4) Evaluer la distance séparant P de G pour n = 5, 10, 25, 50, 100, 1000 et 10000 points.
5) On suppose maintenant que l’on souhaite minimiser la somme des distances au carrés entre les foyers et
le bureau de vote, l’intérêt étant ici de pénaliser fortement les distances élevées. En effet, avec cette méthode,
positionner le bureau de votes à 5 km de deux foyers (5 2 + 5 2 = 50) devient plus intéressant que de le
positionner à 1 km de l’un et à 9 km de l’autre (1 2 + 9 2 = 82). Modifier le programme précédent pour trouver
ce nouveau point P 2 et reprendre la question 4 en remplaçant P par P 2 . Que peut-on en déduire ?
L’on remarquera que le temps de calcul de la distance moyenne augmente très rapidement avec la taille
du problème. La distance entre chaque couple de points doit être mesurée, impliquant n 2 étapes de calculs.
La complexité est dite quadratique. L’exercice 13 donne des pistes pour accélérer ce type d’opérations.

