# déclaration et affectation de chaînes de caractères (strings)
texte1 = "lorem"
texte2 = "ipsum"

# concaténation de chaînes de caractères
texte3 = texte1 + texte2

print(texte3)

texte3 = texte1 + " " + texte2
print(texte3)

# répétition
texte4 = texte1 * 3
print(texte4)

# transtypage (type casting) et concaténation
nombre1 = 123
nombre2 = 3.14
texte5 = str(nombre1) + ", " + str(nombre2) + ", " + texte1
print(texte5)

# formattage de chaîne de caractères avec des f-strings (nécessite python 3.6+)
# f-string = interpolation
texte5 = f"{nombre1}, {nombre2}, {texte1}"
print(texte5)

# formatage plus complexe avec concaténation
texte5 = "nombre1: " + str(nombre1) + ", " + "nombre2: " + str(nombre2) + ", " + "texte1: " + texte1
print(texte5)

# formatage plus complexe avec f-string (nécessite python 3.6+)
# f-string = interpolation
texte5 = f"nombre1: {nombre1}, nombre2: {nombre2}, texte1: {texte1}"
print(texte5)
