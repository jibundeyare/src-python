while True:
    user_age = input("quel est votre âge ? ")

    try:
        user_age = int(user_age)
        break
    except:
        pass

print(user_age)

while True:
    user_has_payment = input("avez-vous un moyen de paiement ? [o/n] ")
    if user_has_payment == 'o':
        user_has_payment = True
        break
    elif user_has_payment == 'n':
        user_has_payment = False
        break
print(user_has_payment)

film1 = (user_age, user_has_payment)
user1 = (16, True)

if film1[0] > 0:
    print("un âge minimum est requis")

    if user1[0] >= film1[0]:
        print("l'utilisateur a l'âge requis")
    else:
        print("l'utilisateur n'a pas l'âge requis")
        print("l'utilisateur ne peut pas regarder le film")
        exit()
else:
    print("un âge minimum n'est pas requis")

if film1[1] == True:
    print("un moyen de paiement est nécessaire")

    if user1[1] == True:
        print("l'utilisateur possède un moyen de paiement")
    else:
        print("l'utilisateur ne possède pas de moyen de paiement")
        print("l'utilisateur ne peut pas regarder le film")
        exit()
else:
    print("un moyen de paiement n'est pas nécessaire")

print("l'utilisateur peut regarder le film")
