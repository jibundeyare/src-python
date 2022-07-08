# exercice-algo-04

# note 4.1
#
# Quand on veut stocker en mémoire une liste, on peut stocker les
# données dans une variable de type `list`.
# Les listes n'ont qu'une seule dimension, c-à-d qu'un seul index permet
# de parcourir toutes les données.

# code 4.1
# stockage de données dans une liste
foo = [3.14, 42, 123]

# affichage de l'élément se trouvant en deuxième position
print(foo[1])

# note 4.2
#
# Quand on veut stocker en mémoire un tableau en deux dimensions (aussi
# appelé matrice), on peut stocker les données dans des listes
# imbriquées.
# Pour accéder aux données, il est nécessaire d'utiliser deux index.

# code 4.2
# stockage de données dans un tableau en deux dimensions
bar = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]

# affichage de l'élément se trouvant dans la troisième colonne de la
# deuxième ligne
print(bar[1][2])

# note 4.3
#
# Mais si l'on sait quelle doit être la largeur du tableau qui stock les
# données en deux dimensions, il est possible de créer une liste capable
# de stocker les données en une dimension.

# code 4.3
# le tableau stock 9 nombres entiers
foo = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

# la liste stock aussi 9 nombres entiers
foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# note 4.4
#
# D'accord, on peut stocker les mêmes données dans une liste à une
# dimension ou un tableau à deux dimension. Mais est-ce possible de
# continuer à accéder aux données dans une liste à une dimension en
# utilisant deux index, comme avec un tableau à deux dimension ?
# La réponse est « oui, c'est possible ».
#
# Voici un tableau qui montre la correspondance entre un index en deux
# dimensions (le premier entier indique la ligne, le deuxième indique la
# colonne) et un index en une dimension pour un tableau de largeur 3 :
#
# | index 2D | index 1D | données |
# |----------|----------|---------|
# | [0][0]   | [0]      | 1       |
# | [0][1]   | [1]      | 2       |
# | [0][2]   | [2]      | 3       |
# | [1][0]   | [3]      | 4       |
# | [1][1]   | [4]      | 5       |
# | [1][2]   | [5]      | 6       |
# | [2][0]   | [6]      | 7       |
# | [2][1]   | [7]      | 8       |
# | [2][2]   | [8]      | 9       |
#
# Votre travail va consister à trouver une fonction qui convertit les
# index en deux dimensions en index en une dimension.

# exo 4.1
#
# Avant de rentrer dans le dur, commençons par quelque chose de plus
# facile.
#
# Essayons de trouver la ligne à partir de l'index en
# une dimension.
#
# Si on connaît la largeur du tableau en deux dimensions, il existe un
# opérateur qui permet de trouver l'index de la ligne en partant d'un
# index en une dimesion.
#
# Écrivez une fonction nommée `get_row()` qui :
#
# - prend un nombre entier nommé `index` (en une dimension) en entrée
# - prend un nombre entier nommé `width` (la largeur) en entrée
# - renvoie un nombre entier indiquant l'index de la ligne
#
# Testez votre fonction avec les valeurs index et width suivantes, elle
# devrait renvoyer la même valeur que le return :
#
# | index | width | return |
# |-------|-------|--------|
# | 0     | 3     | 0      |
# | 1     | 3     | 0      |
# | 2     | 3     | 0      |
# | 3     | 3     | 1      |
# | 4     | 3     | 1      |
# | 5     | 3     | 1      |
# | 6     | 3     | 2      |
# | 7     | 3     | 2      |
# | 8     | 3     | 2      |
#
# Indice : ne cherchez pas quelque chose de compliqué. Le code de la
# fonction est quelque chose du genre `return index X width`. Il faut
# juste trouver le bon opérateur à la place de `X`.
#
# Indice : pour tester votre code, utilisez une boucle `for`.

# réponse 4.1

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
# fonction est quelque chose du genre `return index X width`. Il faut
# juste trouver le bon opérateur à la place de `X`.
#
# Indice : pour tester votre code, utilisez une boucle `for`.

# réponse 4.2

# code 4.4
# Voici un tuple de nombres entiers.
# La virgule sert à séparer les deux valeurs, comme dans une liste.
foo = (1, 2)

# exo 4.3
#
# Si vous avez pu répondre aux questions 4.1 et 4.2, vous allez pouvoir
# écrire une fonction nommée `convert_1d_index_to_2d_index()` qui :
#
# - prend un nombre entier nommé `index` en entrée
# - prend un nombre entier nommé `width` (largeur) en entrée
# - renvoie un tuple de nombres entiers indiquant l'index de la ligne et
#   de la colonne (attention à l'ordre des données)

# réponse 4.3

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
# Indice : pour tester votre code, utilisez une boucle `for`.

# réponse 4.4

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
# Indice : cette fois-ce le code de la fonction est un petit peu
# différent mais rien d'impossible à trouver.
#
# À vous de jouer ;)
#
# Indice : pour tester votre code, utilisez deux boucles `for`
# imbriquées.

# réponse 4.5

