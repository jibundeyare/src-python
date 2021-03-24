# une class nommée Foo avec des variables d'instance :
# - bar
# - baz
# - lorem
# et des méthodes getters et setters
class Foo:
    bar = 123
    baz = 3.14
    lorem = '...'

    def get_bar(self):
        return self.bar

    def set_bar(self, bar):
        self.bar = bar

    def get_baz(self):
        return self.baz

    def set_baz(self, baz):
        self.baz = baz

    def get_lorem(self):
        return self.lorem

    def set_lorem(self, lorem):
        self.lorem = lorem

# import de classes depuis d'autres fichiers
# normalement, les imports se font au tout début des scripts
from lib.pioche import Pioche
from carte import Carte

as_pique = Carte('noir', 'pique', 1)
valet_coeur = Carte('rouge', 'coeur', 11)
six_carreau = Carte('rouge', 'carreau', 6)
roi_trefle = Carte('noir', 'trefle', 13)

print(type(as_pique))
print(as_pique)
print(valet_coeur)
print(f"coleur: {as_pique._couleur}, symbol: {as_pique._symbol}, rang: {as_pique._rang}")
print(as_pique.plus_grand_que(valet_coeur))

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

