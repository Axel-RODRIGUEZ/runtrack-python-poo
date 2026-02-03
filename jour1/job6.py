class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = None

    def vieillir(self):
        self.age += 1   

    def nomer(self):
        if self.prenom == None:
            choice_user = input("Choisissez un nom pour votre animal")
            self.prenom = choice_user
            print(f"Votre animal s'appelle maintenant {self.prenom}")
        else:
            print("Votre animal a déjà un nom")

animal = Animal()

print(animal.age)

animal.vieillir()

print(animal.age)
animal.nomer()