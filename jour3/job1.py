class Ville:
    def __init__(self, nom, nombre):
        self.__nom = nom
        self.__nombre = nombre

    def add_nombre(self, nombre):
        self.__nombre += nombre
        
    def get_nombre(self):
        return self.__nombre

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouter_population()

    def ajouter_population(self):
        self.__ville.add_nombre(1)

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris : {paris.get_nombre()} habitants")
print(f"Population de la ville de Marseille : {marseille.get_nombre()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille) 

print(f"Mise à jour de la population de la ville de Paris : {paris.get_nombre()} habitants")
print(f"Mise à jour de la population de la ville de Marseille : {marseille.get_nombre()} habitants")

    