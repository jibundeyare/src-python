# exercice-03-operateurs.py

# exo 3.1
# Alice est née le 10 février 1988.
# Quelle âge a-t-elle cette année ?
# Ne tenez pas compte du mois, on va partir du principe qu'on est après le 10 février pour ne pas se compliquer la vie.
# Stockez l'année en cours dans une variable nommée `year`.
# Calculez l'âge d'Alice en utilisant les variables `birthyear` et `year` puis stockez le résultat dans une variable nommée `age` et affichez ce résultat.
birthyear = 1988

# réponse 3.1

# exo 3.2
# Bob veut distribuer tous ses bonbons et chocolats à ses amis.
# Il a 15 bonbons, 17 chocolats et 3 amis.
# Combien de bonbons lui restera-t-il ?
# Calculez le reste de bonbons et de chocolats puis stockez les résultats dans les variables `candies_rest` et `chocolates_rest`.
# Affichez ces résultats.
candies = 15
chocolates = 17
friends = 3

# réponse 3.2

# exo 3.3
# Suite de l'exercice précédent.
# Calculez combien de bonbons et chocolats Bob va distribuer par personne et stockez les résultats dans les variables `candies_per_person` et `chocolates_per_person`.
# Affichez ces résultats.
#
# Indice : si vous séchez, reprenez le temps d'examiner la liste des opérateurs arithémtiques.
# Il y en a un qui va tout de suite vous donner la réponse.

# réponse 3.3

# exo 3.4
# Calculez la moyenne des nombres suivants : 1, 1, 2, 3, 5, 8, 13.
# Affectez le résultat à une variable et affichez le résultat.

# réponse 3.4

# exo 3.5
# Alice est en vacance et elle veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune de ses dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,7
# - day5 : 32
# Stockez le nombre de jours dans la variable `days`.
# Calculez le montant total des dépenses en utilisant les variables `day1`, `day2`, etc et stockez le résultat dans la variable `total`.
# Calculez la moyenne des dépenses quotidiennes en utilisant les variables `total` et `days` et stockez le résultat dans la variable `average`.
# Affichez le nombre jours, le montant total et la moyenne des dépenses.

# réponse 3.5

# exo 3.6
# La formule suivante permet de convertir des « miles » en mètres :
#
# meters = miles * 1609.344
#
# Bob est en Angleterre.
# On lui dit que la boulangerie la plus proche est à 3 miles.
# Calculez la distance en mètres avec la variable `miles` puis stockez le résultat dans la variable `meters`.
# Convertissez les mètres en kilo mètres puis stockez le résultat dans la variable `km`.
# Affichez un résultat arrondi de la distance en kilo mètre avec la fonction `round()`.
miles = 3

# réponse 3.6

# exo 3.7
# La formule suivante permet de calculer le montant de la TVA à partir d'un prix « hors TVA » (HTVA) et du taux de la TVA en pourcentage
#
# montant_tva = prix_htva * taux_tva / 100
#
# Ci-dessous la variable price contient le prix HTVA et la variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %).
# Calculez le montant de la TVA à partir du prix HTVA et du taux de TVA, stockez le résultat dans la variable tax_fee puis affichez-le.

price = 314
tax_rate = 20

# réponse 3.7

# exo 3.8
# La formule suivante permet de calculer un prix TTC à partir du prix HTVA et du taux de TVA en pourcentage
#
# prix_ttc = prix_htva + prix_htva * taux_tva / 100
#
# ou encore
#
# prix_ttc = prix_htva * (1 + taux_tva / 100)
#
# La variable price contient le prix HTVA
# La variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %)
# Affichez le prix TVA incluse à partir du prix HTVA et du taux de TVA

price = 271
tax_rate = 20

# réponse 3.8

# exo 3.9
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La marque Alpha propose une tablette à 2,00 euros (pour 120 g).
# La marque Beta propose une tablette à 1,70 euros (pour 100 g).
# Charly a l'intuition que la marque Alpha est plus avantageuse.
# A-t-il raison ?
# Calculez d'abord le poid au kilo (convertir les grammes en kilo donc) et stockez les résultats dans les variables `weight_alpha` et `weight_beta`.
# Puis calculez le prix au kilo avec les variables `price_alpha` et `weight_alpha`, et `price_beta` et `weight_beta` respectivement puis stockez les résultat dans les variables `price_per_kilo_alpha` et `price_per_kilo_beta`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

# réponse 3.9

