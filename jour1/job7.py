class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        self.x -= 1 
        print("L'utilisateur est allé vers la gauche")
    def droite(self):
        self.x += 1 
        print("L'utilisateur est allé vers la droite")
    def haut(self):
        self.y += 1 
        print("L'utilisateur est allé vers le haut")
    def bas(self):
        self.y -= 1 
        print("L'utilisateur est allé vers le bas")
    def position(self):
        return (self.x, self.y)
    
