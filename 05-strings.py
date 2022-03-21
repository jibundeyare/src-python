# Documentation officielle sur les chaînes de caractères
# [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
#
# Documentation officile sur les f-strings
# [string — Common string operations — Python 3 documentation](https://docs.python.org/3/library/string.html#format-string-syntax)

# déclaration et affectation de chaînes de caractères (strings)
texte1 = "lorem"
texte2 = "ipsum"

# Si vous voulez construire une chaîne de caractères en utilisant d'autres variables, il y a deux techniques :
# 1. la concaténation : coller bout à bout plusieurs valeurs (variables et chaînes de caractères en dur)
# 2. l'interpolation : intégrer directement des variables dans une chaîne de caractères

# En python la concaténation suppose que toutes les valeurs soient du type string.
# Pour pouvoir concaténer des nombres entier, des nombres à virgule flottante et des booléens, il faut d'abord les transtyper (type cast) avec la fonction str().

# concaténation de chaînes de caractères
texte3 = texte1 + texte2

print(texte3)

texte3 = texte1 + " " + texte2
print(texte3)

# répétition
texte4 = texte1 * 3
print(texte4)

# concaténation et transtypage (type casting)
nombre1 = 123
nombre2 = 3.14
texte5 = "nombre1: " + str(nombre1) + ", nombre2: " + str(nombre2) + ", texte1: " + texte1
print(texte5)

# interpolation avec une f-string (nécessite python 3.6+)
# f-string : interpolation
texte5 = f"nombre1: {nombre1}, nombre2: {nombre2}, texte1: {texte1}"
print(texte5)

# paramétrage du nombre de chiffres à afficher après la virgule, dans une f-string
# :.2f veut dire afficher comme un float avec deux chiffres après la virgule
# notez la valeur est arrondie
texte5 = f"nombre1: {nombre1:.2f}, nombre2: {nombre2:.2f}, texte1: {texte1}"
print(texte5)


# manipulation de chaîne de caractères

texte6 = 'foo bar baz'

# la fonction len() permet de connaître la longueur d'une chaîne de caractères
print(len(texte6))

# la méthode find() permet de trouver l'index d'une chaîne de caractères présente dans une autre chaîne de caractères
print(texte6.find('bar'))

# la méthode count() permet de compter le nombre d'occurences d'une chaîne de caractères dans une autre
print(texte6.count('ba'))

# la méthode replace() permerde remplacer une chaîne de caractères par une autre
print(texte6.replace('bar', 'foo'))

# La méthode split() permet de scinder une chaîne de caractères en plusieurs éléments.
# Cette fonction prend en paramètre une chaîne de caractères qui sert de séparateur.
# Cette chaîne caractères permet d'indiquer à Python à quel endroit couper la chaîne de caractères.
# Au final la fonction renvoie une liste qui contient des éléments, sauf le séparateur.

# scinder la variable texte6 en utilisant l'espace comme séparateur
liste_mots = texte6.split(' ')
print(liste_mots)

# les index permettent de ne renvoyer qu'une partie d'une chaîne de caractères
# la syntaxe est la suivante : string[start:stop:step]
# start : début
# stop : fin
# step : pas (comme le nombre de pas d'un marcheur)
# Notez bien que pour indiquer les indexes, vous pouvez utiliser des valeurs en dur, des variables voir faire des calculs.

# renvoyer les caractères de l'index 4 (compris) jusqu'à 7 (non compris)
# renvoit 'bar'
print(texte6[4:7])

# renvoyer un caractère sur 2, de l'index 4 (compris) jusqu'à 7 (non compris)
# renvoit 'bar'
print(texte6[4:7:2])

# renvoyer les caractères de l'index 4 (compris) jusqu'à 7 (non compris)
# renvoit 'bar baz'
print(texte6[4:])

# renvoyer les caractères du début jusqu'à l'index 7 (non compris)
# renvoit 'foo bar'
print(texte6[:7])

# renvoyer les caractères de l'index -7 (compris), c-à-d 7 caractères en partant de la fin, jusqu'à la fin
# renvoit 'bar baz'
print(texte6[-7:])

# un « pas » négatif permet d'inverser l'ordre d'une chaîne de caractères
print(texte6[::-1])

# documentation d'une fonction

def addition(a: float, b: float) -> float:
    """Renvoie la somme des nombres a et b

    a float le nombre a
    b float le nombre b
    return float
    """

    return a + b

# affichage de la documentation d'une fonction
# Note : pour sortir de l'aide en ligne, tapez 'q'
help(addition)

