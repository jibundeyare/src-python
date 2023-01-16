# rappel 2.1 :
# - 0 est équivalent à pile
# - 1 est équivalent à face

# code 2.1
# Au jeu de pile ou face, il y a seulement deux issues possibles : pile ou face.
# Pour afficher toutes les issues possibles, on doit utiliser une boucle.
for i in range(0, 2):
    if i == 0:
        print("pile")
    else:
        print("face")

# code 2.2
# Il est possible d'ajouter un compteur, pour savoir combien d'issues existent.

# Variable qui sert de compteur
counter = 0

for i in range(0, 2):
    counter += 1

    if i == 0:
        print("pile")
    else:
        print("face")

print(f"il y a {counter} issues en tout")

# code 2.3
# Si on ne fait qu'un seul lancer, le compteur ne sert pas à grand chose car on sait d'avance qu'il n'y a que 2 issues.
#
# Mais si on joue à pile ou face en faisant plusieurs lancers, il y a plus que 2 issues.
# Avec 2 lancers, on obtient 4 issues possibles :
# - pile & pile
# - pile & face
# - face & pile
# - face & face
#
# Pour afficher tous les cas possibles, on peux utiliser deux boucles imbriquées.

# Premier lancer
for i in range(0, 2):
    # Deuxième lancer
    for j in range(0, 2):
        if i == 0:
            # Le premier lancer donne pile
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("pile", end='')
        else:
            # Le premier lancer donne face
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("face", end='')

        if j == 0:
            # Le deuxième lancer donne pile
            print(" & pile")
        else:
            # Le deuxième lancer donne face
            print(" & face")

