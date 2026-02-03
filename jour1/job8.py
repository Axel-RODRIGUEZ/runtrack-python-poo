import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.circonference = self.rayon * 2 * math.pi
        self.diametre = self.rayon * 2
        self.aire = math.pi * self.rayon * self.rayon
    
    def changer_rayon(self):
        old_rayon = self.rayon
        user_choice = int(input("Veuillez entrer la nouvelle valeur du rayon"))
        self.rayon = user_choice
        print(f"{old_rayon} a été changé par {self.rayon}")
        self.__init__(self.rayon)

    def afficher_infos(self):
        print(f"Information du cercle :\n---------\nRayon : {self.rayon}\nDiamètre : {self.diametre}\nCirconférence : {self.circonference}\nAir : {self.aire}")

    def perimetre(self):
        print(f"La circonférence du cercle est de {self.circonference}")

    def aire_cercle(self):
        print(f"L'aire du cercle est de {self.aire}")

    def diametre_cercle(self):
        print(f"Le diamètre du cercle est de {self.diametre}")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficher_infos()
cercle2.afficher_infos()

cercle1.changer_rayon()
cercle1.afficher_infos()