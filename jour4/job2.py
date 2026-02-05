class Personne:
    def __init__(self):
        self.age = 14

    def afficher_age(self):
        print(self.age)
    
    def bonjour(self):
        print('Hello')

    def modifier_age(self, age):
        self.age = age

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def afficher_age(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere):
        self.__matiere = matiere

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()

eleve.bonjour()
eleve.aller_en_cours()