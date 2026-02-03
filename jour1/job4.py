class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f'Je suis {self.prenom} {self.nom}.'
    
p1 = Personne('Axel', 'Rodriguez')
p2 = Personne ('John', 'Doe')

print(p1.se_presenter())
print(p2.se_presenter())