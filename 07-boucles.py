# Documentation officielle sur la fonction `range()`
# [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#ranges)

# chargement du module math (pour utiliser la fonction "math.floor()")
import math

# boucle `while` infinie car il n'y a pas de condition d'arrêt
# while True:
#     print("boucle infinie")

# boucle `while` avec condition de continuation, qui affiche les nombres de 1 à 10
i = 0
while i < 10:
    # incrémentation de 1
    i += 1
    print("boucle " + str(i))

# boucle `while` avec condition d'arrêt, qui affiche les nombres de 1 à 10
i = 0
while True:
    # incrémentation de 1
    i += 1
    print("boucle " + str(i))

    if i == 10:
        # interruption de la boucle
        break

# boucle `while` classique avec condition de continuation, qui affiche les nombres de 1 à 10
# l'incrémentation se fait en dernier
i = 0
while i < 10:
    print("boucle " + str(i))
    # incrémentation de 1
    i += 1

# boucle `while` à rebours, de 10 à 1
i = 10
while i > 0:
    print("boucle " + str(i))
    # décrémentation de 1
    i -= 1

# boucle `while` à rebours, de 9 à 0
i = 10
while i > 0:
    # décrémentation de 1
    i -= 1
    print("boucle " + str(i))

# boucle `for` en JS
# for (let i = 0; i < 10; i++) {
#     console.log("boucle " + i);
# }

# boucle `for` en PHP
# for ($i = 0; $i < 10; $i++) {
#     echo "boucle ".$i;
# }

# boucle `for` classique, de 1 à 10
for i in range(1, 11):
    print("boucle " + str(i))

# boucle `for` classique, de 0 à 9
for i in range(0, 10):
    print("boucle " + str(i))

# boucle `for` à rebours, de 10 à 1
for i in range(10, 0, -1):
    print("boucle " + str(i))

# boucle `for` à rebours, de 9 à 0
for i in range(9, -1, -1):
    print("boucle " + str(i))

# tous les endroits d'un boucle `while` où vous pouvez placer du code
i = 0
print('avant la boucle')
while i < 10:
    print('dans la boucle')
    i += 1
print('après la boucle')

# tous les endroits d'un boucle `for` où vous pouvez placer du code
print('avant la boucle')
for i in range(0, 10)
    print('dans la boucle')
print('après la boucle')

# boucle `foreach`
items = [123, 2, 42, 3.14, 56]
for item in items:
    print(item)

# boucle `foreach` avec les index associés aux items
for i, item in enumerate(items, 1):
    print(i, item)

# exemple d'utilisation de la fonction `enumerate()`
for i, item in enumerate(items):
    if i == 2:
        print(i, item)

# boucle `foreach` à rebours
for item in reversed(items):
    print(item)

# boucle `foreach` à rebours avec des index
for i in range(len(items) - 1, -1, -1):
    print(i, items[i])

# la variable "cart" contient le prix de produit qu'un client a mis dans son panier de commande
cart = [123, 2, 42, 3.14, 56]

# avec une boucle `foreach`, calculez la somme du panier, ajoutez-y une tva de 20 %, et enfin, calculez le prix moyen des articles hors tva
total = 0
for item in cart:
    total += item
total_tva = total * 1.2
moyenne_article = total / len(cart)

print("total htva", total)
print("total tva", total_tva)
# affichage avec tous les chiffres après la virgule
print("moyenne article htva", moyenne_article)
# affichage avec seuls 2 chiffres après la virgule
print("moyenne article htva", "%.2f" % (moyenne_article))
# affichage avec seuls 2 chiffres après la virgule en utilisant un f string
print(f"moyenne article htva {moyenne_article:.2f}")
# calcul moyenne
moyenne_article_tronquee = math.floor(total / len(items) * 100 ) / 100
