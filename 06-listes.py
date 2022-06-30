# Documentation officielle sur les listes
# [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

# déclaration et affectation d'une liste vide (empty list)
# deux syntaxes différentes pour le même effet
liste1 = []
liste2 = list()

print(liste1)
print(liste2)

# la méthode append() permet d'ajouter une valeur à la fin d'un tableau
# note : dans les autres langages, le terme "push" est plus courant que "append"
# on peut ajouter directement une valeur
liste1.append(123)

# mais on peut aussi ajouter une variable
nombre1 = 42
liste1.append(nombre1)

# un tableau peut contenir différents types de données
liste1.append(3.14)
liste1.append("foo")

print(liste1)

# création d'une liste avec des valeurs (de types différents)
# on peut utiliser directement des valeurs
list3 = [100, 3.14, "foo", True, False, None]

print(list3)

nombre2 = 123
nombre3 = 3.14
texte1 = "lorem"

# mais on peut aussi utiliser des variables
liste4 = [nombre2, nombre3, texte1]

print(liste4)

# ou mélanger les deux
liste5 = [nombre1, texte1, "foo", True]

print(liste5)

# utilisation d'un index pour afficher une valeur particulière d'un tableu
# affichage de la première valeur
print(liste5[0])
# affichage de la dernière valeur
print(liste5[3])

# utilisation d'un index pour supprimer une valeur
del liste5[0]
print(liste5)

# ATTENTION : après un `del` tous les index du tableau sont recalculés !
print(liste5[0])

# la fonction len() permet d'obtenir la longueur d'un tableau, c-à-d le nombre d'éléments d'un tableau
taill_tableau5 = len(liste5)
print(taill_tableau5)

# formule qui permet d'obtenir l'index du dernier élément d'un tableau (s'il n'est pas vide) : "taille du tableau - 1"
dernier_index = len(liste5) - 1
print(dernier_index)

# insérer des éléments au milieu d'un tableau
liste5.insert(1, "foo")
print(len(liste5))
print(liste5)

# utilisation d'un index pour remplacer (réaffecter) une valeur dans un tableau
# c'est comme si on écrasait la valeur avec une nouvelle valeur
liste5[0] = 123

# on peut aussi utiliser une variable pour réaffecter une valeur
texte2 = "baz"
liste5[1] = texte2
print(liste5)

# creation d'un nouveau tableau
liste6 = ['z', 'd', 'r', 'x', 'a']

# affichage du tableau avant modification
print(liste6)

# la fonction sorted() permet d'obtenir une copie d'un tableau triée par ordre alphabétique
liste7 = sorted(liste6)
# le tableau original n'est pas modifié
print(liste6)
# la copie du tableau est triée
print(liste7)

# la méthode sort() (à ne pas confondre avec "sorted()") permet de trier un tableau
# ATTENTION : le tri s'effectue directement sur les données, l'ordre original est donc perdu !
liste6.sort()
print(liste6)

# la méthode pop() permet de supprimer la dernière valeur d'un tableau et d'affecter la valeur supprimée à une variable
# ici, la valeur supprimée est récupérée dans la variable derniere_valeur
derniere_valeur = liste6.pop()
print(liste6)
print(derniere_valeur)

# là par contre, la valeur supprimée n'est récupérée dans aucune variable (du coup elle est perdue)
liste6.pop()
print(liste6)

# concaténation de listes
liste8 = liste5 + liste6
print(liste8)

# fusion de listes
liste5.extend(liste6)
print(liste5)

