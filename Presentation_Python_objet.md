# Aspects pratiques
* 22/02 aprem, 01/03 aprem, 08/03 aprem, 15/03 aprem, 17/03 matin
* 3 salles : M403, L112, L109 (15 places)
* 2 salles pour la dernière séance : M404, L207-208

* PyCharm (ubuntu / windows ?)


# Rappels semestre 1 #
* Tests unitaires
* Exceptions
* Bonnes pratiques
	* Utilisation de la doc en ligne / help()
	* Tests en live
	* Boucle for sur les indices
	* 20 lignes max par fonction
* *args, **kwargs
* imports, modules
* `__main__`



# Classes #
* syntaxe définition
* constructeur
* héritage
* encapsulation
	* tout est public
	* convention : _ pour indiquer que c'est privé
* accesseur, mutateur
* classes abstraites
* quelques méthodes spéciales
    * `__str__`, `__eq__`, `__iter__`, ...
* un fichier par classe


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



