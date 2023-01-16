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

# code 4.4
# Voici un tuple de nombres entiers.
# La virgule sert à séparer les deux valeurs, comme dans une liste.
# Un tuple se comporte comme une liste.
# Sauf qu'on ne peut pas change les valeurs à l'intérieur du tuple comme avec une liste.
foo = (1, 2)

