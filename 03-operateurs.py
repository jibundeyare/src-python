# Documentation officielle sur les opérateurs
# - [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
# - [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#comparisons)

# chargement du module random pour générer des nombres aléatoires
import random

# opérations arithmétiques de base
result = 1 + 2
result = 3 - 4
result = 5 * 6
# division qui renvoie toujours un float (même si le nombre est divisible)
result = 7 / 8

# division entière qui renvoie toujours un integer (division tronquée de tous les chiffres après la virgule)
result = 7 // 8
print(result)

# puissance de 2
# 9 puissance 2 == 9 * 9
result = 9 ** 2
print(result)

# puissance de 3
# 9 puissance 3 == 9 * 9 * 9
result = 9 ** 3
print(result)

# racine de 2
result = 10 ** (1 / 2)
print(result)

# racine de 3
result = 10 ** (1 / 3)
print(result)

# l'opérateur modulo renvoie le reste de la division
# on s'en sert souvent pour tester la parité (pair ou impair) d'un nombre entier

# 14 modulo 2 == 0
result = 14 % 2
print(result)

# 13 modulo 2 == 1
result = 13 % 2
print(result)

# 10 modulo 3 == 1
result = 10 % 3
print(result)

# 5 modulo 3 == 2
result = 5 % 3
print(result)

# 9 modulo 3 == 0
result = 9 % 3
print(result)

# les opérateurs ont un ordre de priorité
# 1. **
# 2. * / % //
# 3. + -

# pour changer l'ordre de priorité on peut utiliser des parenthèses

# on calcul d'abord la division et ensuite la puissance
result = 10 ** (1 / 2)

# on calcul d'abord l'addition et ensuite la multiplication
result = (2 + 3) * 5
print(result) # affiche 25

# alors qu'ici on calcul d'abord la multiplication et ensuite l'addition
result = 2 + 3 * 5
print(result) # affiche 17

# la fonction random.randint() renvoie un nombre entier aléatoir compris entre 1 et 100 inclus
x = random.randint(1, 100)

print("x:", x)

# test de parité (pair ou impair)
print("x modulo 2:", x % 2)
if x % 2 == 0:
    print(x, "est un nombre pair")
else:
    print(x, "est un nombre impair")

# ou
if x % 2:
    print(x, "est un nombre impair")
else:
    print(x, "est un nombre pair")

# test de divisibilité par 3
print("x modulo 3:", x % 2)
if x % 3 == 0:
    print(x, "est divisible par 3")
else:
    print(x, "n'est divisible par 3")

# ou
if x % 3:
    print(x, "n'est divisible par 3")
else:
    print(x, "est divisible par 3")

# opérateurs composés
# ce sont les mêmes que les opérateurs arithmétiques de base mais suivi du signe égal `=`

i = 2

# ajouter 5 à i et affecter le résultat à la variable i
i += 5
# c'est la même chose que
i = i + 5

# soustraire 2 à i et affecter le résultat à la variable i
i += 2
# c'est la même chose que
i = i + 2

# en général, on se sert de ces opérateur pour incrémenter ou décrementer de 1

# incrémenter de 1
c = 0

c = c + 1
# l'opérateur ++ n'existe pas en python mais il est valide dans d'autres langages
# c++
# c'est la même chose que
c += 1 # décrémenter

# décrémenter de 1
c = c - 1
# l'opérateur -- n'existe pas en python mais il est valide dans d'autres langages
# c--
# c'est la même chose que
c -= 1

# on peut aussi composer des multiplications ou des divisions
c *= 2
# c'est la même chose que
c = c * 2

c /= 2
# c'est la même chose que
c = c / 2

# opérateurs de comparaison

# ATTENTION : quand on compare (c-à-d quand on pose une question) il y a deux signes égal `==`
# un seul signe égal `=` c'est pour l'affectation
print(1 == 1)
print(1 == 2)

# test de différence
# certains languages utilisent l'opérateur `<>`
print(1 != 1)
print(1 != 2)

print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

# affectation de tableaux
items_a = [42, 2, 53]
items_b = [42, 2, 53]
items_c = [3, 2, 1]

# comparaison de tableaux
print(items_a == items_b)
print(items_a == items_c)

# affectation de chaînes de caractères
text_a = "hello"
text_b = "hello"
text_c = "bye"

# comparaison de chaînes de caractères
print(text_a == text_b)
print(text_a == text_c)

# dans d'autres langages, il existe des opérateur de comparaison d'identité : une comparaison qui test aussi le type de donnée
# ces opérateurs n'existe pas en python mais sont valides dans d'autres langages (PHP, JS, etc)
# a = 123
# b = '123'
# a === b # type identique et valeurs égales
# a !== b # type différent ou même type mais valeurs différentes
# a >== b # type identiques mais valeur supérieure de la variable a
# a <== b # type identiques mais valeur inférieure de la variable a

# test de présence d'une valeur dans un tableau
# l'opérateur `in` permet de tester la présence d'une valeur dans un tableau

ingredients = ["sucre", "sel", "farine", "carotte"]

print("sucre" in ingredients)
print("cannelle" in ingredients)

# test de présence d'un caractère dans une chaîne de caractères
# l'opérateur `in` permet aussi de tester la présence d'un ou plusieurs caractères dans une chaîne de caractères

word = "cannelle"
# une chaîne de caractères est comme un tableau de caractères
# word = ["c", "a", "n", "n", "e", "l", "l", "e"]

print("a" in word)
print("anne" in word)
print("z" in word)

# l'opérateur `is` permet de tester le type de donnée d'une variable
nombre_a = 123
nombre_b = 3.14

print(type(nombre_a) is int)
print(type(nombre_a) is float)

print(type(nombre_b) is int)
print(type(nombre_b) is float)

if type(nombre_a) is int:
    print("nombre_a est un entier")
else:
    print("nombre_a n'est pas un entier")
    print(type(nombre_a))

if type(nombre_b) is int:
    print("nombre_a est un entier")
else:
    print("nombre_a n'est pas un entier")
    print(type(nombre_b))

