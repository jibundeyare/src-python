# cette classe est utilisée par `12-classes.py`

import random

class Pioche:
    def __init__(self, cartes):
        self._cartes = cartes

    def choisir_au_hasard(self, n):
        cartes = []
        for i in range(0, n):
            carte = random.choice(self._cartes)
            cartes.append(carte)
            self._cartes.remove(carte)

        return cartes

    def remettre(self, cartes):
        self._cartes.extend(cartes)
        cartes.clear()

    def __str__(self):
        return ', '.join([str(carte) for carte in self._cartes])

