# exercice-probabilités-03.py

# Rappel :
# - 0 est équivalent à pile
# - 1 est équivalent à face

# code 3.1
# Pas besoin d'écrire de code pour savoir quelle est la probabilité d'avoir pile avec un seul lancer de pile ou face.
# Mais regardons tout de même cela de plus près.
# Il faut :
# - une boucle
# - un compteur pour accumuler le nombres total d'issues possibles
# - un compteur pour accumuler le nombre d'issues donnant pile
# - un bloc conditionnel pour vérifier quand on a pile

# Le nombre total d'issues
issues = 0
# Le nombre d'issues dont on veut calculer la probabilité
counter = 0

# Premier lancer
for i in range(0, 2):
    issues += 1

    if i == 0:
        # le premier ou le deuxième lancer donne pile
        counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile avec un lancer")

# code 3.2
# Pour savoir quelle est la probailité d'obtenir au moins une fois pile lors de 2 lancers à pile ou face, il faut :
# - deux boucles imbriquées
# - un compteur pour accumuler le nombres total d'issues possibles
# - un compteur pour accumuler le nombre d'issues donnant pile
# - un bloc conditionnel pour vérifier quand on a pile

# Le nombre total d'issues
issues = 0
# Le nombre d'issues dont on veut calculer la probabilité
counter = 0

# Premier lancer
for i in range(0, 2):
    # Deuxième lancer
    for j in range(0, 2):
        issues += 1

        if i == 0 or j == 0:
            # le premier ou le deuxième lancer donne pile
            counter += 1

probability = counter / issues
percentage = probability * 100

print(f"Il y a {percentage:.0f} % de chance d'avoir pile avec deux lancers")

# exo 3.1
# Alice et Bob jouent à pile ou face.
# Alice parie qu'elle va obtenir "pile & pile" en deux lancers.
# Rédigez le code qui indique la probabilité qu'Alice gagne.

# réponse 3.1

# exo 3.2
# Bob parie qu'il va obtenir "pile & pile & pile" ou "pile & pile & face" avec 3 lancers.
# Autrement dit, il pense qu'il va obtenir "pile & pile" lors des deux premiers lancers (sur les 3 en tout).
# Rédigez le code qui indique la probabilité que Bob gagne.

# réponse 3.2

# exo 3.3
# Alice parie qu'elle va obtenir au moins 2 fois pile, avec 3 lancers.
# Avant d'écrire le code, détaillez toutes les issues gagnantes pour Alice.

# réponse 3.3

# exo 3.4
# Rédigez le code qui indique la probabilité que Alice gagne.

# réponse 3.4

