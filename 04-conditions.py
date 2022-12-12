# Documentation officielle sur les opérateurs booléens (opérateurs logiques)
# [Built-in Types — Python 3 documentation](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

# chargement du module random (pour générer des nombres aléatoires)
import random

# Algèbre booléen

# l'opérateur ET logique : `and`

# table de vérité de l'opérateur ET logique
# A       B       A and B
# True    True    True
# False   True    False
# True    False   False
# False   False   False

# moyen mnémo-technique pour se rappeler la table de vérité de l'opérateur ET logique
electricity_off = True
water_off = True
# go_to_holidays : True

electricity_off = False
water_off = True
# go_to_holidays : False

electricity_off = True
water_off = False
# go_to_holidays : False

electricity_off = False
water_off = False
# go_to_holidays : False

# démonstration de l'opérateur `and`
electricity_off = bool(random.randint(0, 1))
water_off = bool(random.randint(0, 1))
print(electricity_off)
print(water_off)

if electricity_off and water_off:
    print("vous pouvez partir en vacances")
else:
    print("vous ne pouvez pas partir en vacances")

# l'opérateur de négation : `not`

# table de vérité de l'opérateur de négation
# A     not A
# True  False
# False True

# exemple d'application qui me dit si je peux partir en vacance ou si j'ai oublié de faire quelque chose
if electricity_off and water_off:
    print("vous pouvez partir en vacances")
elif not electricity_off and water_off:
    print("il faut éteindre l'électricité")
elif electricity_off and not water_off:
    print("il faut couper l'eau")
else:
    print("il faut éteindre l'électricité et couper l'eau")

# l'opérateur OU logique : `or`

# table de vérité de l'opérateur OU logique
# A       B       A or B
# True    True    True
# False   True    True
# True    False   True
# False   False   False

# moyen mnémo-technique pour se rappeler la table de vérité de l'opérateur ET logique
has_bank_card = True
has_cash = True
# go_shopping : True

has_bank_card = False
has_cash = True
# go_shopping : True

has_bank_card = True
has_cash = False
# go_shopping : True

has_bank_card = False
has_cash = False
# go_shopping : False

# démonstration de l'opérateur `or`
has_bank_card = bool(random.randint(0, 1))
has_cash = bool(random.randint(0, 1))
print(has_bank_card)
print(has_cash)

if has_bank_card or has_cash:
    print("vous pouvez partir faire les courses")
else:
    print("vous ne pouvez pas partir faire les courses")

# exemple d'application qui me dit si je peux partir faire des courses ou si j'ai oublié de prendre un moyen de paiement
if has_bank_card and has_cash:
    print("vous avez une carte bancaire et du cash")
elif has_bank_card:
    print("vous avez une carte bancaire")
elif has_cash:
    print("vous avez de cash")
else:
    print("vous ne pouvez pas partir faire les courses")

# Blocs conditionnels

# initialisation d'une variable booléenne
# par convention, on préfixe les variables booléennes avec `is_` ou `has_`
is_day = True

# un bloc conditionnel sans clause `else`
# le code indenté de la section `if` n'est exécuté que si l'expression du `if` est évalué à True
if is_day:
    print("C'est le jour")

# un bloc conditionnel avec clause `else`
# le code indenté de la section `else` n'est exécuté que si l'expression du `if` est évalué à False
if is_day:
    print("C'est le jour")
else:
    print("Ce n'est pas le jour")
    print("(Donc c'est la nuit)")

# Opérateur de négation

# un bloc conditionnel avec une expression négative (l'opérateur de négation `not`)
# on peut utiliser une négation pour poser la question inverse
if not is_day:
    print("Ce n'est pas le jour")
    print("(Donc c'est la nuit)")
else:
    print("Ce n'est pas 'pas le jour'")
    print("(Donc c'est le jour)")

# Blocs conditionnels non binaire

# un bloc conditionnel avec juste un `if` et un `else` est un bloc conditionnel binaire (deux possibilités)
# un bloc conditionnel avec un `if`, un `else` et un ou plusieurs `elif` est un bloc conditionnel non binaire (plus de deux possibilités)

# en python, le mot clé `else if` est abrégé en `elif`

# un bloc conditionnel avec une clause `elif`
# les clauses `elif` permettent de poser des questions dont la réponse n'est pas binaire (pas juste oui / non)
if is_day == None:
    print("Non renseigné")
elif is_day:
    print("C'est le jour")
else:
    print("Ce n'est ni 'non rensigné' ni le jour")
    print("(Donc c'est la nuit)")

# tester une variable pour connaître son encadrement (sa fourchette de valeurs) est un cas typique d'utilisation de clauses `elif`
age = 50

if age < 0:
    print("ereur : âge négatif")
elif age < 12:
    print("enfant")
elif age >= 12 and age < 19:
    print("adolescent")
elif age >= 19 and age < 100:
    print("adulte")
elif age >= 100:
    print("erreur : âge trop élevé")
else:
    print("non renseigné")

# Opérateurs de comparaison

# les opérations avec opérateurs de comparaison renvoient une valeur booléenne
# cette comparaison renvoie False (rappel : age = 50)
print(age < 0)

# cette comparaison renvoie True (rappel : age = 50)
print(age >= 19)

# L'opérateur booléen `and`

# avant de partir en vacance, je dois vérifier que l'eau et le gaz sont coupés
# `water = True` signifie que l'eau est coupée, `water = False` signifie que l'eau n'est pas coupée, idem pour le gaz
# je ne peux partir que si les deux sont coupés
water = True
gas = False

if water and gas:
    print("je peux partir en vacance")
else:
    print("je ne peux pas partir en vacance")

# L'opérateur booléen `or`

# avant de partir faire les courses, je dois vérifier que j'ai bien un moyen de paiement : ma carte bancaire ou de l'argent liquide
# `credit_card = True` signifie que j'ai ma carte bancaire, `credit_card = False` signifie que je n'ai pas ma carte bancaire, idem pour l'argent liquide
# je ne peux partir que si j'ai au moins un des deux moyens de paiement
credit_card = True
cash = False

if credit_card or cash:
    print("je peux partir faire les courses")
else:
    print("je ne peux pas partir faire les courses")

# Combinaisons du même opérateur booléen

# si vous combinez plusieurs fois le même opérateur logique (seulement des `and` ou seulement des `or`) vous n'avez pas besoin d'utiliser de parenthèses

# exemple avec 3 variables
water = True
gas = True
electricity = False

# ici, il faut avoir coupé tous les flux
print(water and gas and electricity)

credit_card = True
cash = True
check = False

# ici, il faut avoir au moins un moyen de paiement
print(credit_card or cash or check)

# Combinaisons d'opérateurs booléen différents

# si vous combinez des opérateurs logiques différents, dans certains cas il faut ajouter des parenthèses pour que le résultat soit correcte

water = False
gas = False
credit_card = True
cash = True

# l'expression suivante comporte une erreur : même si vous n'avez pas coupé l'eau et le gaz, du moment que vous avez un moyen de paiement, vous pourrez partir en vacance
print(water and gas and credit_card or cash)

# pour que l'expression soit correcte, il faut que vous ayez coupé l'eau et le gaz, et par ailleurs que vous ayez au moins un moyen de paiement
# pour corriger, ajoutez des parenthèses
print((water and gas) and (credit_card or cash))

# Exemples d'application

# affichage d'un message en fonction d'une quantité nuémrique
product_quantity = random.randint(0, 5)
print(product_quantity)

if product_quantity == 0:
    print("rupture de stock")
elif product_quantity == 1:
    print("il reste 1 produit")
else:
    print(f"il reste {product_quantity} produits")

# vérifier qu'un nombre est compris entre 25 et 75 inclus
# en notation mathématique : n ∈ [25; 75]
number = random.randint(0, 100)

if number >= 25 and number <= 75:
    print("le nombre est compris entre 25 et 75 inclus")
else:
    print("le nombre n'est pas compris entre 25 et 75 inclus")

# Tests d'autorisation d'accès à un service payant

# trois cas sont possibles :
# 1. l'utilisateur a un compte payant (la période d'essai n'a pas d'importance) : accès autorisé
# 2. l'utilisateur a un compte gratuit, il est en période d'essai : accès autorisé
# 3. l'utilisateur a un compte gratuit, il n'est pas en période d'essai : accès interdit

# activez le cas souhaité en enlevant les dièses

# cas 1.
is_premium = True
is_free_trial = False

# cas 2.
# is_premium = False
# is_free_trial = True

# cas 3.
# is_premium = False
# is_free_trial = False

# solution avec clause `else`
# cette solution est recommandée car elle a l'avantage d'interdire l'accès à toutes les personnes qui ne rentrent pas exactement dans les cases
if is_premium:
    print("accès autorisé")
elif not is_premium and is_free_trial:
    print("accès autorisé")
else:
    print("accès interdit")

# solution alternative avec une clause `elif` au lieu d'une clause `else`
# cette solution, bien qu'elle retranscive exactement le cahier des charges, n'est pas recommandée car elle est moins lisible
if is_premium:
    print("accès autorisé")
elif not is_premium and is_free_trial:
    print("accès autorisé")
elif not is_premium and not is_free_trial:
    print("accès interdit")

# Tests d'éligibilité pour la réception d'une newsletter

# on part du principe que tous les utilisateurs sont abonnés à une newsletter, mais certains ont été ou sont abonnés à la newsletter payante
# trois cas sont possibles :
# 1. l'utilisateur est actuellement abonné à la newsletter payante : newsletter payante
# 2. l'utilisateur n'est actuellement pas abonné à la newsletter payante et ne s'y ait jamais abonné : newsletter gratuite
# 3. l'utilisateur n'est actuellement pas abonné à la newsletter payante mais il s'y ait abonné par le passé: newsletter gratuite + bonus

# activez le cas souhaité en enlevant les dièses

# cas 1.
is_paid_subscriber = True
is_ex_paid_subscriber = False

# cas 2.
# is_paid_subscriber = False
# is_ex_paid_subscriber = False

# cas 3.
# is_paid_subscriber = False
# is_ex_paid_subscriber = True

# solution sans clause `else`
# toutes les conditions sont explicitées dans une clause `if` ou `elif`
# ce type de solution est recommandé si le cahier des charges est relativement complexes et qu'il faut pouvoir contrôler que toutes les clauses du cahier des charges ont bien été retranscrites en code
if is_paid_subscriber:
    print("newsletter payante")
elif not is_paid_subscriber and not is_ex_paid_subscriber:
    print("newsletter gratuite")
elif not is_paid_subscriber and is_ex_paid_subscriber:
    print("newsletter gratuite + bonus")

# solution alternative avec une clause `else`
# la clause `elif` ne teste pas la valeur de la variable `is_paid_subscriber`
# ceci fonctionne très bien ici, mais peut ne pas fonctionner avec un autre cahier des charges donc attention
if is_paid_subscriber:
    print("newsletter payante")
elif is_ex_paid_subscriber:
    print("newsletter gratuite + bonus")
else:
    print("newsletter gratuite")

# Tests d'éligibilité pour la réception d'une newsletter v2

# contrairement à l'exemple précédent, ici on part du principe que les utilisateurs doivent déclarer s'ils veulent une newsletter ou non
# quatre cas sont possibles :
# 1. l'utilisateur ne veut pas recevoir de newsletter : pas de newsletter
# 2. l'utilisateur veut une newsletter et est actuellement abonné à la newsletter payante : newsletter payante
# 3. l'utilisateur veut une newsletter mais n'est actuellement pas abonné à la newsletter payante et ne s'y ait jamais abonné : newsletter gratuite
# 4. l'utilisateur veut une newsletter, il n'est actuellement pas abonné à la newsletter payante mais il s'y ait abonné par le passé: newsletter gratuite + bonus

# activez le cas souhaité en enlevant les dièses

# cas 1.
wants_newsletter = False
is_paid_subscriber = False
is_ex_paid_subscriber = False

# cas 2.
# wants_newsletter = True
# is_paid_subscriber = True
# is_ex_paid_subscriber = False

# cas 3.
# wants_newsletter = True
# is_paid_subscriber = False
# is_ex_paid_subscriber = False

# cas 4.
# wants_newsletter = True
# is_paid_subscriber = False
# is_ex_paid_subscriber = True

# solution avec plusieurs clauses `elif`
# cette solution est recommandée car elle retranscrit exactement le cahier des charges
if not wants_newsletter:
    print("pas de newsletter")
elif wants_newsletter and is_paid_subscriber:
    print("newsletter payante")
elif wants_newsletter and not is_paid_subscriber and not is_ex_paid_subscriber:
    print("newsletter gratuite")
elif wants_newsletter and not is_paid_subscriber and is_ex_paid_subscriber:
    print("newsletter gratuite + bonus")

# solution alternative avec des clauses `if else` imbriquées
# cette solution est idéale si vous voulez découper des clauses complexes et clauses plus simples à comprendre
# son inconvénient est d'être moins compacte
# et si le code devient trop long, paradoxalement, il peu devenir plus complexe que la première solution
if not wants_newsletter:
    # cas où l'utilisateur n'est pas abonné
    print("pas de newsletter")
else:
    # cas où l'utilisateur est abonné
    if is_paid_subscriber:
        # cas où l'utilisateur est abonné à la newsletter payante
        print("newsletter payante")
    else:
        # cas où l'utilisateur n'est pas abonné à la newsletter payante
        if is_ex_paid_subscriber:
            # cas où l'utilisateur a déjà été abonné à la newsletter payante
            print("newsletter gratuite + bonus")
        else:
            # cas où l'utilisateur n'a jamais été abonné à la newsletter payante
            print("newsletter gratuite")

# Tests d'autorisation d'accès à un niveau de jeu

# deux joueurs accumulent un score
# pour pouvoir passer au niveau supérieur, au moins un des deux joueurs doit avoir un score supérieur à 50, sinon la partie est finie game over

# la fonction `random.randint()` renvoie un nombre entier aléatoire
# ici le nombre aléatoire est compris entre 0 et 100 (inclus)
player1_score = random.randint(0, 100)
player2_score = random.randint(0, 100)

print(player1_score)
print(player2_score)

# solution avec deux clauses `if` et `else` seulement
# solution recommandé
if player1_score > 50 or player2_score > 50:
    print("level up")
else:
    print("game over")

# solution non recommandée à cause de la duplication de code (ici, deux fois la ligne `print("level up")`)
# la duplication de code rend le code difficile à maintenir à la longue
if player1_score > 50:
    print("level up")
elif player2_score > 50:
    print("level up")
else:
    print("game over")

# Tests d'autorisation d'accès à un niveau de jeu v2

# cette fois-ci, les deux joueurs doivent avoir un score supérieur à 50 ou au moins un des deux joueurs doit avoir attrapé le bonus "level up" pour pouvoir passer au niveau supérieur

player1_score = random.randint(0, 100)
player2_score = random.randint(0, 100)
# le nombre aléatoire est 0 ou 1 (c-à-d n'a pas le bonus ou a le bonus)
player1_has_bonus = random.randint(0, 1)
player2_has_bonus = random.randint(0, 1)

print(player1_score)
print(player2_score)
print(player1_has_bonus)
print(player2_has_bonus)

# solution avec deux clauses `if` et `else` seulement
# pour la même raison que dans l'exemple précédent, il vaut mieux ne pas utiliser de clause `elif` pour le test du bonus
if (player1_score > 50 and player2_score > 50) or (player1_has_bonus or player2_has_bonus):
    print("level up")
else:
    print("game over")

# Lazy evaluation (évaluation paresseuse)
# Si vous utilisez l'opérayeur booléen "or", dès qu'une valeur True est rencontrée, python arrête d'évaluer les autres valeurs
# Voici un tableau vide
# L'index 0 n'existe pas
foo = []
# Si j'utilise une première valeur True, python n'essaie pas d'accéder à l'index 0
print(True or foo[0])
# Mais si j'utilise une première valeur False, python veut évaluer la valeur suivante et essaie d'accéder à l'index 0, d'où une erreur
print(False or foo[0]) # IndexError: list index out of range

