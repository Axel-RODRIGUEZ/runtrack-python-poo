class Commande:
    def __init__(self, num_com:int, statut_com:str = "en cours"):
        self.__num_com = num_com
        self.__liste_plats_com = []
        self.__statut_com = statut_com

    def ajouter_plat(self, plat:dict):
        self.__liste_plats_com.append(plat)

    def annuler_com(self):
        self.__statut_com = "annulée"

    def total_com(self):
        total_prix = 0
        for plat in self.__liste_plats_com:
            total_prix += plat["prix"]

        return total_prix

    def afficher_com(self):
        total_prix = self.calculer_tva(1.2)

        print(f"Numéro de commande : {self.__num_com}")
        print("Plats de la commande : ")
        for plat in self.__liste_plats_com:
            print(f"- {plat['nom']}")
        print(f"Total à payer : {total_prix}")

    def calculer_tva(self, tva):
        total_prix = self.total_com()

        return total_prix * tva
