class Forme():
    def air():
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def air(self):
        air = self.longueur * self.largeur
        return air
    
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def air(self):
        air = 3.14 * self.rayon * self.rayon
        return air