# @todo ajouter des print pour mieux voir les sections
# @todo check commentaires

# déclaration et affectation d'une variable
# initialisation d'une variable = la première affectattion de valeur
foo = 123

# affichage d'une variable
print(foo)

# nombre entier = integer
nombre1 = 42
nombre2 = -2

print(nombre1)
print(nombre2)

# nombre à virgule flottante = float (number)
nombre3 = 3.14
nombre4 = 123.0

print(nombre3)
print(nombre4)

# texte ou chaîne de caractères = string (of characters)
texte1 = "Hello World!"
texte2 = "<h1>I love Python!</h1>"

print(texte1)
print(texte2)

# saut de ligne = new line
texte3 = "ligne 1\nligne 2"

print(texte3)

# saut de ligne = new line
texte4 = """ligne 1
ligne 2"""

print(texte4)

# un caractère échapé = escaped character
texte5 = "\n"
texte6 = "\\"
texte7 = "oui\\non"
texte8 = "oui\non"

print(texte5)
print(texte6)
print(texte7)
print(texte8)

# chaîne de caractères = string
# doubles quotes pour le texte
texte10 = "lorem ipsum"
# simples quotes poour des labels, des clés ou des codes
texte9 = 'lorem ipsum'

print(texte9)
print(type(texte9))
print(texte10)
print(type(texte10))

# réaffectation et changement de type de données
# attention : ceci n'est pas possible dans tous les langages
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

# valeur booléenne = boolean value
boolean1 = True
boolean2 = False

print(boolean1)
print(boolean2)

# valeur nulle = null value
null1 = None

print(null1)

# transtypage de variables = type casting
nombre5 = 2
print(type(nombre5))
print(nombre5)

# int -> float
nombre5 = float(nombre5)
print(type(nombre5))
print(nombre5)

nombre6 = 3.14
print(type(nombre6))
print(nombre6)

# float -> int
nombre6 = int(nombre6)
print(type(nombre6))
print(nombre6)

nombre7 = 456
print(type(nombre7))
print(nombre7)

# int -> str
nombre7 = str(nombre7)
print(type(nombre7))
print(nombre7)

nombre8 = 3.14
print(type(nombre8))
print(nombre8)

# float -> str
nombre8 = str(nombre8)
print(type(nombre8))
print(nombre8)

# bool -> int
boolean3 = True
boolean3 = int(boolean3)
boolean4 = False
boolean4 = int(boolean4)
print(boolean3)
print(boolean4)

# null -> int
null2 = None
# attention : génère l'erreur "TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'" 
# null2 = int(null2)

# null -> str
null2 = str(null2) # str(None) == "None"
print(null2)
