class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculer_prix_TTC(self):
        prix_TTC = self.prixHT * self.TVA
        return prix_TTC

    def afficher(self):
        return f'Nom du produit : {self.nom}\nPrix HT du produit : {self.prixHT}\nTVA du produit : {self.TVA}'
    
    def modifier_nom(self):
        old_nom = self.nom
        user_choice = input("Choisissez un nouveau nom : ")
        self.nom = user_choice
        return f'{old_nom} a été changé en {self.nom} ! '
    
    def modifier_prix(self):
        old_prix = self.prixHT
        user_choice = int(input("Choisissez un nouveau prix : "))
        self.prixHT = user_choice
        return f'{old_prix} a été changé en {self.prixHT} ! '