from carte import Carte

as_pique = Carte('noir', 'pique', 1)
valet_coeur = Carte('rouge', 'coeur', 11)

print(type(as_pique))
print(as_pique)
print(valet_coeur)
print(f"coleur: {as_pique._couleur}, symbol: {as_pique._symbol}, rang: {as_pique._rang}")
print(as_pique.plus_grand_que(valet_coeur))
