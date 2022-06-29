# une class nommée Foo
# avec des variables d'instance :
#   - bar
#   - baz
# des variables de classe :
#   - lorem
#   - ipsum
# des méthodes getters et setters d'instance
# et des méthodes getters et setters de classe
class Foo:
    # variables de classe
    lorem = 'aaa'
    ipsum = 'bbb'

    # constructeur
    def __init__(self, bar, baz):
        # variables d'instance
        self.bar = bar
        self.baz = baz

    # méthode getter d'instance
    def get_bar(self):
        return self.bar

    # méthode setter d'instance
    def set_bar(self, bar):
        self.bar = bar

    # méthode getter d'instance
    def get_baz(self):
        return self.baz

    # méthode setter d'instance
    def set_baz(self, baz):
        self.baz = baz

    # méthode getter de classe
    @classmethod
    def get_lorem(cls):
        return cls.lorem

    # méthode setter de classe
    @classmethod
    def set_lorem(cls, lorem):
        cls.lorem = lorem

    # méthode getter de classe
    @classmethod
    def get_ipsum(cls):
        return cls.ipsum

    # méthode setter de classe
    @classmethod
    def set_ipsum(cls, ipsum):
        cls.ipsum = ipsum

f = Foo()
g = Foo()

# lecture de variables d'instance
print(f.get_bar())
print(g.get_bar())

# modification d'une variable d'instance
f.set_bar(234)
print(f.get_bar())
print(g.get_bar())

# lecture d'une variable de classe
print(f.get_lorem())
print(g.get_lorem())

# modification d'une variable de classe
f.set_lorem('ccc')
print(f.get_lorem())
print(g.get_lorem())

# import de classes depuis d'autres fichiers
# normalement, les imports se font au tout début des scripts
from lib_jeu_cartes import Carte
from lib_jeu_cartes import Jeu
from lib_jeu_cartes import Pioche

as_pique = Carte('noir', 'pique', 1)
valet_coeur = Carte('rouge', 'coeur', 11)
six_carreau = Carte('rouge', 'carreau', 6)
roi_trefle = Carte('noir', 'trefle', 13)

print(type(as_pique))
print(as_pique)
print(f"coleur: {as_pique._couleur}, symbole: {as_pique._symbole}, rang: {as_pique._rang}")
print(valet_coeur)
print(as_pique.plus_grand_que(valet_coeur))

jeu = Jeu()
jeu.regle_as_au_top()
print(jeu.plus_grand_que(as_pique, valet_coeur))

pioche = Pioche([as_pique, valet_coeur, six_carreau, roi_trefle])
print("pioche:", pioche)

cartes = pioche.choisir_au_hasard(2)

print("cartes choisies au hasard: ")
for carte in cartes:
    print('- ' + str(carte))

print("pioche:", pioche)

pioche.remettre(cartes)
print("cartes choisies au hasard:", cartes)
print("pioche", pioche)

