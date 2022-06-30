# exercice-algo-02

# note 2.1
#
# Connaissez-vous la suite de Fibonacci ?
# Cette suite est calculée en additionnant les nombres des deux rangs
# précédent. Le rang 0 et le rang 1 sont fixés à 0 et 1 respectivement.
#
# Voici la formule de la suite :
# F0 = 0
# F1 = 1
# Fn = Fn-2 + Fn-1
#
# Un démonstration rendra les choses plus claires.
#
# On a dit que les deux premiers rangs (c-à-d nombres) de la suite de
# Fibonacci étaient 0 et 1.
# On a donc :
# F0 = 0 et F1 = 1
# 
# Pour obtenir F2, on additionne F0 et F1.
# On a donc :
# F2 = F0 + F1 = 0 + 1 = 1
# Ce qui donne F2 = 1
#
# Pour obtenir F3, on additionne F1 et F2.
# On a donc :
# F3 = F1 + F2 = 1 + 1 = 2
# Ce qui donne F3 = 2
#
# Et ainsi de suite.
#
# Maintenant on peut généraliser.
# Pour obtenir Fn, on addition Fn-2 et Fn-1.
# Ce qui donne la formule :
# Fn = Fn-2 + Fn-1

# exo 2.1
#
# Ajoutez les 10 premiers nombres de la suite de Fibonacci, que vous
# aurez calculé « à la main », dans une liste. Puis affichez cette
# liste en utilisant une boucle de type « for each ».
# Note : la suite doit démarre à 0.

# réponse 2.1

# exo 2.2
#
# Reprenez votre boucle de type « for each » et modifiez-là de façon à
# utiliser un index et la fonction `range()` pour parcourir le liste
# des nombres de Fibonacci.

# réponse 2.2

# exo 2.3
#
# Écrivez une fonction nommé `fibonacci_1_3()` qui :
# - renvoie `0` si on lui passe `0` en paramètre
# - renvoie `1` si on lui passe `1` en paramètre
# - renvoie `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 2.3

# exo 2.4
#
# Reprenez votre fonction `fibonacci_1_3`, renommez-là `fibonacci_1_4`.
# Puis modifiez-là de façon à ce que la fonction :
# - renvoie la somme de `fibonacci_1_4(0)` et
# `fibonacci_1_4(1)` si on lui passe `2` en paramètre.
# - renvoie `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 2.4

# exo 2.5
#
# Reprenez votre fonction `fibonacci_1_4`, renommez-là `fibonacci_1_5`.
# Puis modifiez-là de façon à ce que la somme de `fibonacci_1_4(0)` et
# `fibonacci_1_4(1)` utilise la vraiable `n` au lieu de valeurs
# constantes.
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.
#
# Indice : comment obtenir `0` quand `n == 2` ? Comment obtenir `1`
# quand `n == 2` ?
#
# ATTENTION : n'oubliez pas que maintenant vous devez appeler la
# fonction `fibonacci_1_5()` et plus `fibonacci_1_4()`.

# réponse 2.5

# exo 2.6
#
# Reprenez votre fonction `fibonacci_1_5`, renommez-là `fibonacci_1_6`.
# Vous êtes mûr pour finir le travail et rendre la fonction
# opérationnelle au delà de `2`.
#
# Appelez votre fonction dans une boucle qui va de `0` à `10` en
# utilisant un index et la fonction `range()`.

# réponse 2.6

# exo 2.7
#
# Ça vous semble bon ? On va vérifier en créant un test.
#
# Appelez la fonction `fibonacci_1_6()` dans une boucle qui va de `0` à
# 10` en utilisant un index et la fonction `range()`. Utilisez cet index
# pour récupérer le nombre du rang correspondant dans la liste
# `fibonacci_numbers` puis comparez le résultat de votre fonction. S'il
# y a une différence, affichez un message d'erreur suivi du rang et des
# deux valeurs.

# réponse 2.7

