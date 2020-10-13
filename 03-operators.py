# chargement du module random pour générer des nombres aléatoires
import random

# opérations arith de base
result = 1 + 2
result = 3 - 4
result = 5 * 6
# division qui renvoit toujours un float (même si le nombre est divisible)
result = 7 / 8

# division entière (division tronquée de tous les chiffres après la virgule)
result = 7 // 8
print(result)

# puissance de 2
result = 9 ** 2
print(result)

# puissance de 3
result = 9 ** 3
print(result)

# racine de 2
result = 10 ** (1 / 2)
print(result)

# racine de 3
result = 11 ** (1 / 3)
print(result)

# 5 modulo 3 donne 2
result = 5 % 3
print(result)

x = random.randint(1, 100)

print("x:", x)

# test de parité (pair ou impair)
print("x modulo 2:", x % 2)
if x % 2:
    print(x, "est un nombre impair")
else:
    print(x, "est un nombre pair")

# test de divisibilité par 3
print("x modulo 3:", x % 2)
if x % 3:
    print(x, "n'est divisible par 3")
else:
    print(x, "est divisible par 3")

# opérateurs composés
# ce sont les mêmes que les opérateurs arithmétiques de base mais suivi du signe égal "="
i = 2
# ajouter 5 à i et affecter le résultat à i
i += 5

# c'est la même chose que
i = i + 5

# opérateurs de comparaison

# attention, quand on compare (c-à-d quand on pose une question) il y a deux signes égal "=="
# un seul signe égal "=" c'est pour l'affectation
print(1 == 1)
print(1 == 2)

# test de différence
# certains languages utilisent ce symbole "<>"
print(1 != 1)
print(1 != 2)

print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

items_a = [42, 2, 53]
items_b = [42, 2, 53]
items_c = [3, 2, 1]

print(items_a == items_b)
print(items_a == items_c)

text_a = "hello"
text_b = "hello"
text_c = "bye"

print(text_a == text_b)
print(text_a == text_c)

# test de présence d'une valeur dans un tableau
ingredients = ["sucre", "sel", "farine", "carotte"]

print("sucre" in ingredients)
print("cannelle" in ingredients)

# test de présence d'un caractère dans une chaîne de caractères
word = "cannelle"
print("a" in word)
print("z" in word)

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
