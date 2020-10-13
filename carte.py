# cette classe est utilisée par `12-classes.py`

class Carte:
    def __init__(self, couleur, symbol, rang):
        self._couleur = couleur
        self._symbol = symbol
        self._rang = rang

    def plus_grand_que(self, c):
        return self._rang > c._rang

    def plus_petit_que(self, c):
        return self._rang < c._rang

    def egal_a(self, c):
        return self._rang == c._rang

    def __str__(self):
        return f"{self._couleur} {self._symbol} {self._rang}"

