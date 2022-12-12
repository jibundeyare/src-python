# Documentation officielle sur les type `int` et `float`
# [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

# déclaration et affectation d'une variable
# initialisation d'une variable : la première affectattion de valeur
foo = 123

# affichage d'une variable
print(foo)

# nombre entier : integer
nombre1 = 42
nombre2 = -2

print(nombre1)
print(nombre2)

# nombre à virgule flottante : float (number)
nombre3 = 3.14
nombre4 = 123.0

print(nombre3)
print(nombre4)

# texte ou chaîne de caractères : string (of characters)
texte1 = "Hello World!"
texte2 = "<h1>I love Python!</h1>"

print(texte1)
print(texte2)

# saut de ligne : new line
texte3 = "ligne 1\nligne 2"

print(texte3)

# saut de ligne : new line
texte4 = """ligne 1
ligne 2"""

print(texte4)

# un caractère échapé : escaped character
texte5 = "\n"
texte6 = "\\"
texte7 = "oui\\non"
texte8 = "oui\non"

print(texte5)
print(texte6)
print(texte7)
print(texte8)

# chaîne de caractères : string
# doubles quotes pour le texte
texte10 = "lorem ipsum"
# simples quotes poour des labels, des clés ou des codes
texte9 = 'lorem ipsum'

print(texte9)
print(type(texte9))
print(texte10)
print(type(texte10))

# réaffectation et changement de type de données
# ATTENTION : ceci n'est pas possible dans tous les langages
foo = 42
print(foo)
print(type(foo))

foo = 0.123
print(foo)
print(type(foo))

foo = "lorem ipsum"
print(foo)
print(type(foo))

# print permet d'afficher des variables de type différents 
print(nombre1, nombre3, texte1)

# valeur booléenne : boolean value
boolean1 = True
boolean2 = False

print(boolean1)
print(boolean2)

# valeur nulle : null value
null1 = None

print(null1)

# transtypage de variables : type casting

nombre5 = 2
print(type(nombre5))
print(nombre5)

# int vers float
nombre5 = float(nombre5)
print(type(nombre5))
print(nombre5)

nombre6 = 3.14
print(type(nombre6))
print(nombre6)

# float vers int
nombre6 = int(nombre6)
print(type(nombre6))
print(nombre6)

nombre7 = 456
print(type(nombre7))
print(nombre7)

# int vers str
nombre7 = str(nombre7)
print(type(nombre7))
print(nombre7)

nombre8 = 3.14
print(type(nombre8))
print(nombre8)

# float vers str
nombre8 = str(nombre8)
print(type(nombre8))
print(nombre8)

# bool vers int
boolean3 = True
boolean3 = int(boolean3)
boolean4 = False
boolean4 = int(boolean4)
print(boolean3)
print(boolean4)

# null vers int
null2 = None
# provoque l'erreur : TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# null2 = int(null2)
# provoque l'erreur : TypeError: float() argument must be a string or a number, not 'NoneType'
# null2 = float(null2)

# null vers str
null2 = str(null2) # str(None) == "None"
print(null2)

# permutation de variables
a = 123
b = 42
print(a, b)

# permutation de variables spécifique à python
a, b = b, a
print(a, b)

# permutation de variables avec une variable temporaire
tmp = b
b = a
a = tmp
print(a, b)

# permutation de variables sans variable temporaire
# ATTENTION : valable seulement pour les valeurs numériques
a = a + b
b = a - b
a = a - b
print(a, b)

# ATTENTION : les nombres à virgule flottante ne se comportent pas toujours comme on s'y attendrait
0.1 + 0.1 + 0.1 == 0.3 # False

# de même pour l'arrondi des nombres à virgule flottante
round(0.5) # 0
round(1.5) # 2

# pour additionner correctement des nombres décimaux ou les arrondir, il faut utiliser la librairie "decimal"
import decimal
from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3') # True

# demande d'utilisation du mode d'arrondi habituel, c-à-d ROUND_HALF_UP
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
Decimal("0.5").quantize(Decimal("1")) # Decimal('1')
Decimal("1.5").quantize(Decimal("1")) # Decimal('2')

# voir 
# - [Pourquoi 0.1 + 0.2 n'est pas égal à 0.3 en informatique ??? - YouTube](https://www.youtube.com/watch?v=CDYiwshriWw&ab_channel=Grafikart.fr)
# - [Floating Point Visually Explained](https://fabiensanglard.net/floating_point_visually_explained/)
# - [How to Round Numbers in Python – Real Python](https://realpython.com/python-rounding/#the-decimal-class) pour plus d'infos
# - [15. Floating Point Arithmetic: Issues and Limitations — Python 3.10.2 documentation](https://docs.python.org/3/tutorial/floatingpoint.html)
# - [decimal — Decimal fixed point and floating point arithmetic — Python 3.10.2 documentation](https://docs.python.org/3/library/decimal.html)

