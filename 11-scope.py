# scope /  portée des variables

foo = 123

def afficher():
    # foo = 200
    baz = 42
    print(foo)
    # provoque l'erreur "UnboundLocalError: local variable 'foo' referenced before assignment"
    # foo = 333
    print(baz)

afficher()

# provoque l'erreur "NameError: name 'baz' is not defined"
# print(baz)

print(foo)

if False:
    lorem = 123

# provoque l'erreur "NameError: name 'lorem' is not defined"
# print(lorem)

while False:
    lorem = 234

# provoque l'erreur "NameError: name 'lorem' is not defined"
# print(lorem)

for i in range(0, 0):
    lorem = 345

# provoque l'erreur "NameError: name 'lorem' is not defined"
# print(lorem)

ipsum = 123

def ma_fonction():
    return 'foo'

# la bonne pratique est de modifier une variable globale depuis le scope global
# (à moins de faire de la programmation orientée objet)
ipsum = ma_fonction()

