class Forme():
    def air():
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        super().__init__()
        self.largeur = largeur
        self.longueur = longueur

    def air(self):
        air = self.longueur * self.largeur
        return air