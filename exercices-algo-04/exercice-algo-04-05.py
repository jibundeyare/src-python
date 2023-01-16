# exo 4.5
#
# Maintenant nous sommes dans le dur.
#
# Essayons de trouver l'index en une dimension à partir de l'index de la
# ligne et de l'index de la colonne.
#
# Écrivez une fonction nommée `convert_2d_index_to_1d_index()` qui :
#
# - prend un nombre entier nommé `row` (la ligne) en entrée
# - prend un nombre entier nommé `column` (la colonne) en entrée
# - prend un nombre entier nommé `width` (la largeur) en entrée
# - renvoie un nombre entier qui est l'index (en une dimension) qui
#   indique exctamenent où se trouve la donnée dans la liste
#   
# Testez votre fonction avec les valeurs row, column et width suivantes,
# elle doit renvoyer la même valeur que le return :
#
# | row | column | width | return |
# |-----|--------|-------|--------|
# | 0   | 0      | 3     | 0      |
# | 0   | 1      | 3     | 1      |
# | 0   | 2      | 3     | 2      |
# | 1   | 0      | 3     | 3      |
# | 1   | 1      | 3     | 4      |
# | 1   | 2      | 3     | 5      |
# | 2   | 0      | 3     | 6      |
# | 2   | 1      | 3     | 7      |
# | 2   | 2      | 3     | 8      |
#
# À vous de jouer ;)
#
# Indice : ne cherchez pas quelque chose de compliqué. Le code de la
# fonction s'écrit en une seule ligne. C'est quelque chose du genre
# `return row X width Y column`. Il faut juste trouver les bons
# opérateurs à la place de `X` et `Y`.
#
# Indice : pour tester votre code, utilisez **deux** boucles `for`
# imbriquées et utilisez `3` pour le `width`.. La première boucle est
# pour indiquer la ligne, la deuxième pour indiquer la colonne.

# réponse 4.5

