```
Les listes de compréhension

    Appliquer un traitement sur les éléments d'un ensemble

nouvelle_liste = [e**2 for e in liste]


Est mieux que :

nouvelle_liste = []
for e in liste:
    nouvelle_liste.append(e**2)

Les listes de compréhension


>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> liste = [e+1 for e in liste]
>>> t_stop = time.time()
>>> print(t_stop - t_start)
0.5306060314178467
```
=> l'exemple ne correspond pas et il n'y a pas de comparaisons (timings)


```
Les context managers
```
=> pas de rapport direct avec les exceptions.
Ce n'est pas une définition de cette fonctionnalité (le lien avec les exceptions).


```
Python objet
Déclaration d'une classe
```
=> Peut etre expliquer (aussi simplement que possible) la notion d'héritage et
héritages multiples (et faire comprendre pourquoi on hérite (en python3.x)
forcément de la classe native 'object').

==> t'en parle après dans 'Héritage'.
```
toutes les classes héritent de la classe object
```
du coup c'est pas forcément vrai, comme le montre ton exemple qui suit juste après:
```
>>> class ClasseMere(object):
...     def une_methode(self):
...         print("Je suis dans la classe mère")
...
>>> class ClasseFille(ClasseMere):
...     pass
```
=> ClasseFille n'hérite pas (directement) de la classe object.

Je ne sais pas trop comment introduire ces notions d'héritages,
de résolutions d'objects, etc ... sans etre trop techniques ...
C'est une problématique assez large et compliquée en Python
et c'est ce qui fait une grande particularité de ce langage
(les choix qui ont été adoptés pour l'héritages multiples et la résolution des conflits
via MRO (https://www.python.org/download/releases/2.3/mro/)).
Enfin bon, je te laisse gérer le positionnement du curseur :p


```
Lecture/écriture d'attributs

    Décorateur sur les fonctions
        @property pour faire comme si la méthode était un attribut
        @attribut.setter pour faire comme si l'on affectait une valeur à l'attribut
```
=> Du coup tu parles des décorateurs à ce niveau,
et cette notion a un rapport plus direct (voir direct tout court) avec les context managers (beaucoup plus que les exceptions).
Faudrait peut etre regrouper ces deux notions (context manager et décorateurs).
