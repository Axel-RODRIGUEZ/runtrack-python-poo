class Livre:
    def __init__(self, titre, auteur, nbr_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_pages = nbr_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbr_pages(self):
        return self.__nbr_pages
    def set_nbr_pages(self, nbr_pages):
        if type(nbr_pages) is int:
            self.__nbr_pages = nbr_pages
            return
        else:
            print("Erreur : Veuillez entrer un nombre entier")
            return
    
    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.__disponible == True:
            print("Le livre a été emprunté !")
            self.__disponible = False
        else:
            print("Le livre a déjà été emprunté !")

    def rendre(self):
        if self.verification() == False:
            print("Le livre a été rendu !")
            self.__disponible = True
            
        else:
            print("Le livre n'est pas emprunté.")

livre = Livre('test', 'Axel', 213)

livre.emprunter()

livre.rendre()

livre.rendre()