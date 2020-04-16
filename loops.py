# while True:
#     print("loop")

i = 0
while True:
    # incrémentation de 1
    i += 1
    print("loop" + str(i))
    if i == 3:
        break

# boucle while classique, de 1 à 10
i = 0
while i < 10:
    # incrémentation de 1
    i += 1
    print("loop" + str(i))

# boucle while classique, de 0 à 9
i = 0
while i < 10:
    print("loop" + str(i))
    # incrémentation de 1
    i += 1

# boucle while à rebours, de 10 à 1
i = 10
while i > 0:
    print("loop" + str(i))
    # décrémentation de 1
    i -= 1

# boucle while à rebours, de 9 à 0
i = 10
while i > 0:
    # décrémentation de 1
    i -= 1
    print("loop" + str(i))

# boucle "for" en JS
# for (let i = 1; i < 11; i++) {
#     console.log("loop" + i);
# }

# boucle "for" classique, de 1 à 10
for i in range(1, 11):
    print("loop" + str(i))

# boucle "for" classique, de 0 à 9
for i in range(0, 10):
    print("loop" + str(i))

# boucle "for" à rebours, de 10 à 1
for i in range(10, 0):
    print("loop" + str(i))

# boucle "for" à rebours, de 9 à 0
for i in range(9, -1):
    print("loop" + str(i))
