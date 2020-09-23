# définition
def hello():
    print("Hello World!")

# appel
hello()

def moyenne(valeurs):
    somme = 0

    for valeur in valeurs:
        somme += valeur

    return somme / len(valeurs)

nombres = [100, 123, 3.14, 46]
m = moyenne(nombres)
print("moyenne des nombres:", m)

points = [100, 143, 167]
m = moyenne(points)
print("moyenne des points:", m)

def addition(a, b):
    return a + b

a = 1
b = 2
resultat = addition(a, b)
print(resultat)

resultat = addition(3, 4)
print(resultat)

def incrementer(a, b=1):
    return a + b

a = 0
a = incrementer(a)
print(a)
a = incrementer(a, 2)
print(a)
a = incrementer(a, b=3)
print(a)

def ma_fonction(a, b=1, c=2):
    return a + b + c

resultat = ma_fonction(1, b=2)
resultat = ma_fonction(1, c=3)
# modifie b mais pas c
resultat = ma_fonction(1, 2)
# modifie b (2) et c (3)
resultat = ma_fonction(1, 2, 3)

# destructured assignment
def ma_fonction2(a, b):
    return a + b, a - b

addition, soustraction = ma_fonction2(1, 2)
print(addition)

def modifier_valeur(valeurs):
    valeurs[1] = 'foo'

# le tableau original est modifié car la variable est transmise par référence
modifier_valeur(nombres)
print(nombres)

# une copie du tableau est transmise à la fonction
# c'est cette copie qui est modifié
modifier_valeur(points.copy())
print(points)

## type hinting

def ma_fonction3(a:float, b:float) -> bool:
    return a > b

resultat = ma_fonction3('foo', 'bar')

# les fonctions sont des variables comme les autres
# on peut les copier dans une autre variable
py_max = max

# la fonction "max()" existe dans les cope global
def max():
    pass

print(py_max(points))

max = py_max

print(max(points))
