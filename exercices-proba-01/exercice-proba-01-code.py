# [xkcd: Frequentists vs. Bayesians](https://xkcd.com/1132/)

import random

# code 1.1
# L'appel à la fonction random.randint(0, 1) renvoie un nombre entier aléatoire compris entre 0 et 1 inclus.
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

