class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def get_info(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}")

    def demarrer():
        print("Attention, je roule")
    
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.porte = 4

    def get_info(self):
        super().get_info()
        print(f"Nombre de porte : {self.porte}")
    
    def demarrer():
        print("Attention, je roule en voiture")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def get_info(self):
        super().get_info()
        print(f"Nombre de roue : {self.roue}")

    def demarrer():
        print("Attention, je roule en moto")