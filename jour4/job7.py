import random

class Carte:
    def __init__(self, nom, valeur, couleur):
        self.nom = nom
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.preparer_paquet()
    
    def preparer_paquet(self):
        for i in liste_couleur:
            for j in liste_valeur:
                carte = Carte(j["nom"], j["valeur"], i)
                self.paquet.append(carte)

        for k in self.paquet:
            print(k.nom, k.couleur)

    def distribuer_carte(self):

        i = 0
        cartes_joueur = []

        while i < 2:
            carte_rand = random.choice(self.paquet)
            cartes_joueur.append(carte_rand) 
            i += 1  
            self.paquet.remove(carte_rand)

        return cartes_joueur
    
    def prendre_carte(self):
        nombre = random.randint(1, 2)
        i = 0
        cartes_pioche = []

        while i < nombre:
            carte_rand = random.choice(self.paquet)
            cartes_pioche.append(carte_rand) 
            i += 1  
            self.paquet.remove(carte_rand)
        
        for carte in cartes_pioche:
            print(f"La pioche à donné le {carte.nom} de {carte.couleur}. Valeur de la carte : {carte.valeur}")

        return cartes_pioche
    
    def check_croupier(self, liste, nombre):
        total = nombre

        for carte in liste:
            total += carte.valeur

        if total >= 17:
            return self.croupier_total(total)
        else:
            return None

    def perdu(self, total):
        print(f"Vous avez perdu ! Le total de points était de {total}")
        return True

    def croupier_total(self, total):
        print(f"Le Croupier a atteint {total} ! Arrêt des jeux.")
        return True

    def update(self, liste):
        total = 0
        for carte in liste:
            total += carte.valeur

        if total > 21:
            return self.perdu(total)
        else:
            return None
        
    def check(liste, liste_croupier):
        total = 0
        total_croupier = 0

        for j in liste_croupier:
            total_croupier += j.valeur

        for carte in liste:
            total += carte.valeur

        if total > 21:
            print(f"Vous avez perdu. Total : {total}")
            return True

        elif total < 21 and total < total_croupier :
            print(f"Vous avez perdu ! Le croupier à un score plus élevé.\n Score du croupier : {total_croupier}\nVotre score : {total}")
            return True
        else:
            print(f"Vous avez gagné ! Vous avez un score plus élevé que le croupier.\n Score du croupier : {total_croupier}\nVotre score : {total}")
            return True
    
liste_couleur = ["Pique", "Coeur", "Trèfle", "Carreau"]
liste_valeur = [
    {"nom" : "As", "valeur" : 1 }, 
    {"nom" : "2", "valeur" : 2 },
    {"nom" : "3", "valeur" : 3 },
    {"nom" : "4", "valeur" : 4 },
    {"nom" : "5", "valeur" : 5 },
    {"nom" : "6", "valeur" : 6 },
    {"nom" : "7", "valeur" : 7 },
    {"nom" : "8", "valeur" : 8 },
    {"nom" : "9", "valeur" : 9 },
    {"nom" : "10", "valeur" : 10 },
    {"nom" : "Roi", "valeur" : 11 },
    ]
jeu = Jeu()
croupier = 0

while True:
    print("Bienvenue dans le Black Jack ! ")

    user_choice = input("1: Jouer\n2: Quitter\n\n")

    if user_choice == "1":
        cartes_joueur = jeu.distribuer_carte()
        croupier_pioche = []
        for carte in cartes_joueur:
            print(f"Vous avez obtenu le {carte.nom} de {carte.couleur}. Valeur de la carte : {carte.valeur}")

        check = jeu.update(cartes_joueur)
        if check:
            break

        while True:
            user_choice2 = input("---------\n1: Prendre des cartes supplémentaires\n2: Passer son tour\n\n")
            
            if user_choice2 == "1":
                cartes_joueur.extend(jeu.prendre_carte())
                check = jeu.update(cartes_joueur)
                if check == True:
                    quit()
                
                print("Au tour du croupier...")

                croupier_pioche.extend(jeu.prendre_carte())
                ckeck = jeu.check_croupier(croupier_pioche, croupier)

                if check == True:
                    jeu.check(cartes_joueur, croupier_pioche)
                    if final_check == True:
                        quit()

            
            elif user_choice2 == "2":

                print("Vous passez ! Au tour du croupier..")

                croupier_pioche.extend(jeu.prendre_carte())
                check = jeu.check_croupier(croupier_pioche, croupier)
                if check == True:
                    final_check = Jeu.check(cartes_joueur, croupier_pioche)
                    if final_check == True:
                        quit()

                    
            else:
                print("Erreur, veuillez réessayer")
                continue

    elif user_choice == "2":
        quit()

    else:
        print("Erreur, veuillez réessayer.")
        continue