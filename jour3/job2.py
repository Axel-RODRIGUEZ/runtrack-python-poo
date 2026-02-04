class CompteBancaire:
    def __init__(self, id_compte, nom, prenom, solde, decouvert):
        self.__id_compte = id_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def add_solde(self, nombre):
        self.__solde += nombre
    
    def get_decouvert(self):
        return self.__decouvert
    
    def afficher(self):
        info = f'ID du compte : {self.__id_compte}.\nNom du client : {self.__nom}.\nPrénom du client : {self.__prenom}.\nSolde du compte : {self.__solde}.'
        return info
    
    def afficher_solde(self):
        return f'Solde du compte : {self.__solde}.'
        
    def versement(self, versement):
        self.__solde += versement
        return f'Versement effectué. Nouveau solde : {self.__solde}'

    def virement(self, virement, nombre):
        if (self.__solde < nombre and self.__solde != 0) or (self.__decouvert == True):
            virement.add_solde(nombre)
            self.__solde -= nombre
            return f'Le virement de {nombre} euro(s) a bien été fait à {virement.get_nom()} {virement.get_prenom()}'
        
        elif self.__solde != 0 and nombre > self.__solde:
            return "Erreur : Votre solde n'a pas l'argent nécessaire au retrait."
        else:
            return "Erreur : Votre solde est à zéro."

    def retrait(self, retrait):
        if (self.__solde != 0 and retrait <= self.__solde) or (self.__decouvert == True):
            self.__solde -= retrait
            return f'Vous avez bien retiré {retrait}. Nouveau solde : {self.__solde}'
        elif self.__solde != 0 and retrait > self.__solde:
            return "Erreur : votre solde n'a pas l'argent nécessaire au retrait."
        else:
            return "Erreur : Votre solde est à 0"
    
    def agios(self, nbr_jour):
        if self.__decouvert == True and self.__solde < 0:
            montant_decouvert = abs(self.__decouvert)
            montant_agios = montant_decouvert * nbr_jour / 365
            return f"Vous devez {round(montant_agios, 2)} euros."
        elif self.__decouvert == True and self.__solde >= 0:
            return f"Erreur : Votre solde n'est pas à découvert. Vous ne devez pas d'Agios"
        else:
            return f"Erreur : Votre compte n'a pas de découvert possible, vous n'avez donc aucun Agios à payer."

compte = CompteBancaire(1, "John", "Doe", 120, True)
compte2 = CompteBancaire(2, "Axel", "Rodriguez", -160, True)

print(compte2.agios(800))