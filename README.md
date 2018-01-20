# Python_ENSG_Geomatique

Cours de programmation avec Python initialement conçu et donné aux étudiants de l'[ENSG Géomatique](http://www.ensg.eu).


## Pré-requis

A priori aucun, si ce n'est l'envie d'apprendre.


## Ce que ce cours contient

Ce cours est constituée d'un support de cours général introduisant les bases du langage Python (caractéristiques du langage, syntaxes de base...) et quelques notions plus avancées (programmation orientée objet, connexion à une base de données...). Une présentation reprend dans les grandes lignes les mêmes éléments que le cours complet.

Enfin des exercices / TP accompagnent ces supports de cours. Ils ne sont pas ordonnées en reprenant la même logique que le plan du cours, mais les notions abordées sont rappelées en introduction de chacun d'eux.

Les corrections ne sont pas systématiquement présentes (voir rarement en fait :-) mais vous pouvez toujours m'envoyer un message si vous avez besoin d'un conseil).


## Regénérer les slides et pdf par vous même
Les supports de cours sont rédigés en markdown. La génération des documents finaux (cours et TP en pdf, présentations en HTML) fait appel à l'utilitaire [pandoc](https://pandoc.org/). Pour les présentations la libraire [reveal.js](https://revealjs.com/#/) doit avoir été téléchargée pour bénéficier de la mise en page correcte.

Les lignes de commande permettant de générer les documents à partir des sources sont listées ci-dessous :

* Le support de cours général :
```
pandoc -s -N --listings --template=template/template.latex -o Cours_Python.pdf Cours_Python.md
```

* La présentation :
```
pandoc -s -t html5 --template=template/ign-ensg-revealjs.html --section-divs -o Presentation_Python.html Presentation_Python.md
```

* Les TPs :
```
pandoc -s -N --listings --template=template/template_tp.latex -o TP/TP_cryptographie.pdf TP/TP_cryptographie.md
```
