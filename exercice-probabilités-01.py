# exercice-probabilités-01.py

# [xkcd: Frequentists vs. Bayesians](https://xkcd.com/1132/)

import random

# code 1.1
# L'appel à la fonction random.randint(0, 1) renvoit un nombre entier aléatoire compris entre 0 et 1 inclus.
number = random.randint(0, 1)

# code 1.2
# Pour savoir si la variable "number" vaut 1, je peux utiliser un bloc conditionnel.
if number == 0:
    print("le nombre vaut 0")

# code 1.3
# Pour savoir quel nombre la variable "number" vaut, je peux utiliser une boucle.
for i in range(0, 2):
    if number == i:
        # affichage avec interpolation de la variable au moyen d'une "f-string"
        print(f"le nombre vaut {number}")

# exo 1.1
# Alice et Bob veulent jouer à pile ou face.
# - si la variable "head_or_tail" vaut 0, cela équivaut à pile
# - si elle vaut 1, cela équivaut à face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

head_or_tail = random.randint(0, 1)

# réponse 1.1

# exo 1.2
# Alice et Bob veulent jouer aux dés.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

dice = random.randint(1, 6)

# réponse 1.2

# exo 1.3
# Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.

alice = random.randint(1, 3)
bob = random.randint(1, 3)
print(alice, bob)

# réponse 1.3

