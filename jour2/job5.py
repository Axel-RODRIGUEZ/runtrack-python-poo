class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False 
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele
    
    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        if type(annee) is int and annee > 1900:
            self.__annee = annee
        else:
            print("Erreur : Année invalide")

    def get_km(self):
        return self.__km
    
    def set_km(self, km):
        if km >= self.__km:
            self.__km = km
        else:
            print("Erreur : On ne peut pas baisser le kilométrage.")   

    def demarrer(self):
        if self.verifier_plein() >= 6:
            if self.__en_marche:
                print("La voiture est déjà démarrée")
            else:
                print("La voiture démarre !")  
                self.__en_marche = True
        else:
            print("La voiture n'a plus assez de carburant.")

    def arreter(self):
        if self.__en_marche:
            print("La voiture s'arrête !")
            self.__en_marche = False
        else:
            print("La voiture est déjà arrêtée")  
            
    def verifier_plein(self):
        return self.__reservoir