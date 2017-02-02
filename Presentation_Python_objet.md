% Python objet
% Division des enseignements en informatique
% 2016


# Quelques rappels #
## L'itération en Python ##
* Itérer sur les éléments pas sur les indices

```
liste = [2, 5, 4, 8, 1]

for i in range(len(liste)):
	liste[i] += 1
```

```
liste = [2, 5, 4, 8, 1]

for e in liste:
	e += 1
```


## L'itération en Python ##

```
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> for e in liste:
...	    e += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
0.8220820426940918
```


## L'itération en Python ##

```
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> for i in range(len(liste):
...	    liste[i] += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
1.3101308345794678
```


## L'itération en Python ##

```
>>> liste = [1 for i in range(10000000)]
>>> t_start = time.time()
>>> i = 0
>>> while i < len(liste):
...	    liste[i] += 1
...     i += 1
...
>>> t_stop = time.time()
>>> print(t_stop - t_start)
2.6622660160064697
```


## *args et **kwargs ##

* Passer un nombre indéterminé d'arguments à une fonction
* Arguments passés sous forme de tuple

```
def somme(*args):
	s = 0
	for arg in args:
		s += arg
	return s
```


## *args et **kwargs ##

* Passer un nombre indéterminé d'arguments nommés à une fonction
* Arguments passés sous forme de dictionnaire

```
def presentation(**kwargs):
	for key, val in kwargs:
		print("{} => {}".format(key, value))
```

```
>>> presentation(nom="Mousse", prenom="Emma", age=22)
age => 22
prenom => Emma
nom => Mousse
```


## Calculs virgules fixes/flottants ##



## Les messages d'erreurs ##

* Exemple, le fichier `script.py` contient :
 
```
def une_fonction(a):
    return 1 / a
 
def une_autre_fonction():
    une_fonction(0)
 
une_autre_fonction()
```

## Les messages d'erreurs ##

* Lecture du message d'erreur de bas en haut (*pile des appels*)

```
Traceback (most recent call last):
  File "script.py", line 7, in <module>
    une_autre_fonction()
  File "script.py", line 5, in une_autre_fonction
    une_fonction(0)
  File "script.py", line 2, in une_fonction
    return 1 / a
ZeroDivisionError: division by zero
```


## Les exceptions ##

> Mécanisme pour gérer des erreurs survenues lors de l'exécution d'un programme.

* Apporter une solution à un problème bloquant
* Eviter d'interrompre le programme
* D'autres solutions, mais c'est la manière de faire en Python


## Les exceptions les plus fréquentes ##

* `NameError` : la variable ou fonction manipulée n'est pas déclarée
* `TypeError` : le type de la variable ne permet pas d'effectuer l'opération demandée
* `ValueError` : le type est correct, mais pas la valeur
* `ZeroDivisionError` : division par zéro
* `IndexError` : tentative d'accès à un élément d'une séquence avec un indice qui n'existe pas 
* `KeyError` : tentative d'accès à un élément d'un dictionnaire avec une clé qui n'existe pas
* `FileNotFoundError` : le fichier n'existe pas
* `IOError` : erreur lors de la manipulation d'un fichier
* `SyntaxError` : erreur de syntaxe (indentation, parenthèse...)


## Soulever une exception ##

* Mot-clé `raise`
* Lever volontairement une exception quand une condition particulière se produit 

```
def ma_fonction(age):
	if age < 0:
		raise ValueError("'age' doit etre positif")
	# suite de la fonction
```

```
>>> ma_fonction(-2)
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
  File "<interactive input>", line 3, in ma_fonction
ValueError: 'age' doit etre positif !
```


## Traiter d'une exception ##

* Mots-clé `try / except`

```
try:
	# ce qui peut produire une exception
except NomException:
	# ce qu'il faut faire si l'exception se déclanche
```

```
liste = ['toto', 'titi', 'tata'...]
try:
	choix = liste[10 // i]
except ZeroDivisionError:
	print("Division par zero impossible")
	choix = liste[0]
except IndexError:
	print("Probleme d'index")
	choix = liste[len(liste)]
```

## Traiter d'une exception ##

* `finally` et `else`

```
try:
	# ce qui peut produire une exception
except NomException:
	# ce qu'il faut faire si l'exception se déclanche
else:
	# ce qu'il faut faire si aucune exception n'a été levée
finally:
	# ce qui sera exécuté dans tous les cas, qu'une exception ai eu lieu ou pas
```


## Traiter une exception ##

```
try:
	f = open('fichier.txt', 'w')
	# écriture dans le fichier
except IOError:
	print("Probleme lors de l'écriture du fichier")
else:
	print("Ecriture OK")
finally:
	f.close()
```


## Les context managers ##

* Simplifier les choses quand la gestion des exceptions devient lourde 

```
try:
    with open('fichier.txt', 'w') as f:
        # écriture dans le fichier
except (IOError, FileNotFoundError):
    # gérer l'erreur
```


## Documentation ##
* Expliquer ce que font les fonctions, classes, modules...
* Indispensable pour rendre le code exploitable par d'autres

```
def ma_fonction(a, b):
	"""
	Ligne générale de description de ce que fait la fonction

	Description plus détaillé, si besoin, de comment la fonction
	fait ce qu'elle fait, de ce qu'elle utilise...

	:param a: description de ce que contient a
	:type a: type de la valeur attendue dans a
	:param b: description de ce que contient b
	:type b: type de la valeur attendue dans b
	:return: description de ce que retourne la fonction
	:returntype: type de la valeur retournée par la fonction 
	"""
```


## Les tests unitaires ##



## Modules et imports ##



## Bonnes pratiques ##
* Utilisation de la documentation
	* comment utiliser une fonction ? `help(fonction)`
	* quelles sont les fonctions de ce module ? `dir(module)`
	* où trouver de la doc en ligne ? <https://docs.python.org/3.5/>


## Bonnes pratiques ##
* `nom_de_variable`, `nom_de_fonction`, `NomDeClasse`
* `a + b` (et pas `a+b`)
	* respecter les conventions c'est faciliter la lecture 
* 20 lignes max par fonction
	* au delà c'est rarement compréhensible !
* 1 fonction = 1 tâche
	* découper en sous-fonction pour rendre plus compréhensible/maintenable/testable
* 1 fichier = 1 classe
* Utiliser bloc `if __name__ == '__main__':` pour exécuter le code
	* la console ne sauvegarde pas vos test
* Testez votre code *en live*



# Python objet #
## Définition d'une classe ##

* Utilisation du mot-clé `class`

```
class MaClasse(object):
	...
	...
```


## Constructeur ##

* Méthode appelée pour instancier les objets

```
class MaClasse(object):
	def __init__(self, param1, param2...):
		...
```

* Instanciation

```
mon_objet = MaClasse(param1, param2...)
```

## Les attributs ##

* Mot-clé `self` pour faire référence à la classe elle-même


## Les méthodes ##

* le premier paramètre est toujours self
* il correspond à l'objet avant le point lors de l'appel


## L'héritage ##

> Principe permettant de créer une classe à partir d'une autre

* Nom de la classe mère entre parenthèses lors de la définition
	* *toutes les classes héritent donc de la classe `object`*

```
class ClasseFille(ClasseMere):
	...
```


## L'encapsulation ##

> Principe visant à cacher les détails de l'implémentation à l'utilisateur

* En Python : **tout est public**
* Convention : `_` avant le nom de l'attribut pour indiquer qu'il est privé


## Lecture/écriture d'attributs ##

* Décorateur sur les fonctions

`@property` pour faire comme si la méthode était un attribut

`@attribut.setter` pour gérer l'écriture


## Les classes abstraites ##

> Classe qui ne peut être instanciée

* Notion de classe abstraite inexistante en Python
* Astuce : lever une exception dans le constructeur

```
class MaClasseAbstraite(object):
	def __init__(self, param1, param2...):
		raise NotImplementedError
```

## Personnaliser le comportement des objets ##

* méthodes spéciales
    * `__str__`, `__eq__`, `__iter__`, ...




# Bases de données #
## SQLite ##
* Moteur de BDDR
* Moteur intégré au programme
* BDD dans un seul fichier indépendant de la plateforme
* Librairie standard de Python

```
import sqlite3
```

## L'objet connection ##
* Représente une connection à une base de données
* Interface pour valider (commit) ou annuler (rollback) les transactions
* Génère les curseurs

```
conn = sqlite3.connect("user/password@database")

conn.commit()  # valider transaction
conn.rollback()  # annuler transaction
conn.close()  # fermer la connection
```

syntaxe avec with

## L'objet curseur ##
* Représente une instruction SQL sous format texte
* Utilisé pour parcourir les résultats d'une requête SQL

```
curs = conn.cursor()

curs.execute(sql_string [, parameters])  # execute requete sql
```

## Les requêtes prises en charge ##
* Tous types de requêtes SQL acceptés

```
curs.execute("CREATE TABLE ...")
curs.execute("UPDATE ...")
curs.execute("INSERT INTO ...")
curs.execute("SELECT ...")

```

## Passage de paramètres ##
* Utilisation du caractère `?`
* Valeur des paramètres sous forme de tuple

```
query = "SELECT nom, prenom FROM personne WHERE naissance > ? AND sexe = ?"
curs.execute(query, (2000, 'M'))
```

## Résultats des requêtes SQL ##
* Séquence d'objets Python

```
curs.execute(select_query)
results = curs.fetchall()
for row in results:
    ...
```

## Exemples ##
```
>>> import sqlite3
>>> conn = sqlite3.connect('dbase1')
>>> curs = conn.cursor()
>>> curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
>>> curs.rowcount
1
```

## Exemples ##
```
>>> rows = [['Tom', 'mgr', 100000],
...         ['Kim', 'adm', 30000],
...         ['pat', 'dev', 90000]]

>>> for row in rows:
...     curs.execute('insert into people values (? , ?, ?)', row)
...

>>> conn.commit()
```

## Exemples ##
* Utilisation de `fetchall()` pour avoir tous les résultats d'un coup

```
>>> curs.execute('select * from people')
>>> for row in curs.fetchall():
...     print(row)
...
('Bob', 'dev', 5000)
('Sue', 'mus', 70000)
('Ann', 'mus', 60000)
('Tom', 'mgr', 100000)
('Kim', 'adm', 30000)
('Pat', 'dev', 90000)
```

## Exemples ##
* Possibilité de ne retenir que certaines colonnes en Python (semblable aux dictionnaires)

```
>>> curs.execute('select * from people')
>>> for (name, job, pay) in curs.fetchall():
...     print(name, ':', pay)
...
Bob : 5000
Sue : 70000
Ann : 60000
Tom : 100000
Kim : 30000
Pat : 90000
```

## Exemples ##
* Idem en utilisant la position des colonnes

```
>>> curs.execute('select * from people')
>>> names = [rec[0] for rec in curs.fetchall()]
>>> names
['Bob', 'Sue', 'Ann', 'Tom', 'Kim', 'Pat']
```

## Exemples ##
* Utilisation fe `fetchone()` pour n'avoir qu'une ligne de résultat à la fois

```
>>> curs.execute('select * from people')
>>> while True:
...     row = curs.fetchone()
...     if not row:
...         break
...     print(row)
...
('Bob', 'dev', 5000)
('Sue', 'mus', 70000)
('Ann', 'mus', 60000)
('Tom', 'mgr', 100000)
('Kim', 'adm', 30000)
('pat', 'dev', 90000)
```

## Exemples ##
* `rowcount` indique le nombre de lignes impactées par la requête

```
>>> curs.execute('update people set pay=? where pay <= ?', [65000, 60000])
>>> curs.rowcount
3
>>> curs.execute('select * from people')
>>> curs.fetchall()
[('Bob', 'dev', 65000), ('Sue', 'mus', 70000), ('Ann', 'mus', 65000), ('Tom', 'mgr',
100000), ('Kim', 'adm', 65000), ('pat', 'dev', 90000)]
```

## Exemples ##
* Accès à la description des colonnes (`curs.description`)

```
>>> curs.execute('select * from people')
>>> colnames = [desc[0] for desc in curs.description]
>>> for row in curs.fetchall():
...     for name, value in zip(colnames, row):
...         print(name, '\t=>', value)
...     print()
...
name => Sue
job  => mus
pay  => 70000

name => Ann
job  => mus
pay  => 65000

```

## Exemples ##
* Possible de faire en Python ce que font de grosses requêtes compliquées

```
>>> query = ("select name from people where job = 'devel' and "
...                "pay > (select avg(pay) from people where job = 'devel')")
>>> curs.execute(query)
>>> curs.fetchall()
[('kim',)]
```

```
>>> curs.execute("select name, pay from people where job = 'devel'")
>>> result = curs.fetchall()
>>> avg = sum(rec[1] for rec in result) / len(result)
>>> print([rec[0] for rec in result if rec[1] > avg])
['kim']
```


## Mapping classes-bdd ##
* Classiquement
    * Classe = table
    * Objet = ligne
    * Attribut = colonne



