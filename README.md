# Python_ENSG_Geomatique #

Cours de programmation avec Python de l'ENSG Géomatique


## Préalables ##

* installation de pandoc
* ...

## Création des pdf / html ##

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
