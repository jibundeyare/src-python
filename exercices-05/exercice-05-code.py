# code 5.1
# La méthode `str.split()` permet de scinder une chaîne de caractères en tableau de chaînes de caractères en utilisant un séparateur
# Example : ici on scinde une chaîne de caractères en utilisant l'espace ' ' comme séparateur
print("foo bar baz".split(' '))

# code 5.2
# En python, un saut de ligne dans une chaîne de caractères peut être obtenu en utilisant un caractère échappé
my_text1 = "texte\nmulti\nligne"
# Ou en utilisant une chaîne de caractères multiligne
my_text2 = """texte
multi
ligne"""
# Mais dans la mémoire de python, les deux chaînes de caractères sont encodées de la même façon
print('\n' in my_text1)
print('\n' in my_text2)

# code 5.3
# La méthode `str.find()` permet de retrouver la position d'une chaîne caractères dans une autre chaîne de caractères
print("foo bar baz".find('bar'))
# Quand `str.find()` ne trouve pas de résultat, la méthode renvoie `-1`
# Mais on peut aussi borner la recherche.
# Exemple : ici on démarre la recherche à partir de l'index 5
print("foo bar baz".find('bar', 5))

