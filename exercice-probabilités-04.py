# exercice-probabilités-04.py

import random

# code 4.1
# Il existe un type de données particulier en Python : le tuple.
my_tuple = ('foo', 123)

# code 4.2
# Les tuples ressemblent aux listes car on peut y lire des données à la façon d'une liste.
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

# code 4.3
# Mais à la différence des listes, une fois que l'on a créé un tuple, on ne peut plus le changer.
# Si vous activez le code suivante, vous verrez l'erreur "# TypeError: 'tuple' object does not support item assignment"
# my_tuple[0] = 'lorem'

# code 4.4
# Cela ne vous empêche pas de changer complètement le contenu de la variable.
# Mais cela ne change rien au fait qu'on ne pas changer le tuple.
my_tuple = None

# code 4.5
# Malgré cette limitation, les tuples sont pratiques pour créer des objets composites à partir de données de base ("int", "float", "bool", "str")
# Par exemple, on peut s'en servir pour modéliser un jeu de carte à jouer.
cards = []

# Dans un jeu de cartes, il y a des cartes dans 4 couleurs.
# Nous allons utiliser une convention pour choisir les couleurs :
# - cœur : 0
# - carreau : 1
# - pique : 2
# - trèfle : 3
for i in range(0, 4):
    # Ensuite il y a les cartes de 1 à 10 et les têtes.
    # Nous allons utiliser une convention pour représenter les têtes :
    # - valet : 11
    # - reine : 12
    # - roi : 13
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))

print(cards)

# code 4.6
# Voici comment mélanger le jeu de carte.
random.shuffle(cards)

# code 4.7
# Voici comment tirer au hasard une carte du jeu.

# sélection d'une carte au hasard
card = random.choice(cards)
print(card)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)

# code 4.8
# Voici comment remettre une carte dans le jeu.
cards.append(card)

# code 4.9
# Voici comment tirer 1 carte du jeu, la mettre dans le paquet d'Alice et au final les remettre dans le jeu.

# le paquet de carte d'Alice (au début, il est vide)
alice_cards = []

# sélection d'une carte au hasard
card = random.choice(cards)
# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)
# ajout de la carte dans le paquet d'Alice
alice_cards.append(card)

# remise des cartes d'alice dans le jeu
cards.extend(alice_cards)
# suppression de toutes les carte d'Alice de son paquet
alice_cards.clear()

# exo 4.1 : Rédigez le code qui affiche la valeur et la couleur de chaque carte du jeu.

# réponse 4.1

# exo 4.2 : Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Puis Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le nombre de cartes qui restent dans le jeu et enfin remettez toutes les cartes dans le jeu.

# réponse 4.2

# exo 4.3 : Bob tire 3 cartes au hasard (sans les remettre dans le jeu) et les met dans son paquet.
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le paquet de Bob, le nombre de cartes qui restent dans le jeu et remettez toutes les cartes dans le jeu.

# réponse 4.3

# exo 4.4 : Alice et Bob parient en jouant aux cartes.
# Voici comment se déroule le jeu :
# 1. Bob mélange les cartes, puis Alice tire trois cartes.
# 2. Elle parie que si un 3 (de n'importe quelle couleur) ou deux cœurs figurent parmi les cartes tirées, elle gagne.
# 3. Alice remets ses cartes dans le jeu, le mélange à nouveau, puis Bob tire 3 cartes.
# 4. Il parie que si un 7 (de n'importe quelle couleur) ou deux piques figurent parmi les cartes tirées, il gagne.
# 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
# Ils décident de faire trois manches.
# Rédigez le code qui modélise ce jeu et indiquez qui sera le gagnant des trois manches.

# réponse 4.4

