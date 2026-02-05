class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        perimetre = 2 * (self.__longueur + self.__largeur)
        return perimetre

    def surface(self):
        surface = self.__longueur * self.__largeur
        return surface
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepiped(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        volume = self.get_longueur() * self.get_largeur() * self.hauteur
        return volume
        