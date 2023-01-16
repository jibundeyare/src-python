# exo 4.4
#
# Maintenant, essayons de trouver l'index en une dimension à partir de
# l'index de la ligne.
#
# Écrivez une fonction nommée `get_row_start()` qui :
#
# - prend un nombre entier nommé `row` (la ligne) en entrée
# - prend un nombre entier nommé `width` (la largeur) en entrée
# - renvoie un nombre entier qui indique l'index (en une dimension) où
#   commence la ligne
#
# Testez votre fonction avec les valeurs row et width suivantes, elle
# doit renvoyer la même valeur que le return :
#
# | row | width | return |
# |-----|-------|--------|
# | 0   | 3     | 0      |
# | 1   | 3     | 3      |
# | 2   | 3     | 6      |
#
# Indice : de nouveau, ne cherchez pas quelque chose de compliqué. Le
# code de la fonction est quelque chose du genre `return row X width`.
# Il faut juste trouver le bon opérateur à la place de `X`.
#
# Indice : pour tester votre code, utilisez une boucle `for` avec `range()` pour le `row` et utilisez `3` pour le `width`.

# réponse 4.4

