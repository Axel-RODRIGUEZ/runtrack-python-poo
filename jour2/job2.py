class Livre:
    def __init__(self, titre, auteur, nbr_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_pages = nbr_pages

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
        
livre = Livre('Test', 'Axel', 213)

print(livre.get_nbr_pages())

livre.set_nbr_pages(312)

print(livre.get_nbr_pages())

livre.set_nbr_pages(7.5)

print(livre.get_nbr_pages())
