# exo 4.2
#
# Cette fois-ci, essayons de trouver la colonne à partir de l'index en
# une dimension.
#
# Si on connaît la largeur du tableau en deux dimensions, il existe un
# opérateur qui permet de trouver l'index de la colonne en partant d'un
# index en une dimesion.
#
# Écrivez une fonction nommée `get_column()` qui :
#
# - prend un nombre entier nommé `index` en entrée
# - prend un nombre entier nommé `width` (largeur) en entrée
# - renvoie un nombre entier indiquant l'index de la colonne
#
# Testez votre fonction avec les valeurs index et width suivantes, elle
# devrait renvoyer la même valeur que le return :
#
# | index | width | return |
# |-------|-------|--------|
# | 0     | 3     | 0      |
# | 1     | 3     | 1      |
# | 2     | 3     | 2      |
# | 3     | 3     | 0      |
# | 4     | 3     | 1      |
# | 5     | 3     | 2      |
# | 6     | 3     | 0      |
# | 7     | 3     | 1      |
# | 8     | 3     | 2      |
#
# Indice : ne cherchez pas quelque chose de compliqué. Le code de la
# fonction s'écrit en une seule ligne. C'est quelque chose du genre
# `return index X width`. Il faut juste trouver le bon opérateur à la
# place de `X`.
#
# Indice : pour tester votre code, utilisez une boucle `for` avec `range()` pour l'index et utilisez `3` pour le `width`.

# réponse 4.2

