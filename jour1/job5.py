class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_les_points(self):
        return f'La position du point est {self.x} {self.y}'
    
    def afficher_x(self):
        return f'Voici x : {self.x}'
    
    def afficher_y(self):
        return f'Voici y : {self.y}'
    
    def changer_x(self):
        old_x = self.x
        self.x = input("Veuillez entrer la nouvelle valeur")
        print(f"{old_x} a été changé en {self.x}")

    def changer_y(self):
        old_y = self.y
        self.y = input("Veuillez entrer la nouvelle valeur")
        print(f"{old_y} a été changé en {self.y}")

