class Personnage():
    def __init__(self, nom:str, vie:int, force:int):
        self.nom = nom 
        self.vie = vie
        self.force = force

    def attaquer(self, cible:object):
        cible.vie -= self.force


class Jeu():
    def __init__(self):
        self.niveau = self.choisir_niveau()
        self.lancer_jeu()

    def choisir_niveau(self):
        choix_user = input("Choisissez le niveau de difficulté\n\n1 : Facile\n2 : Intermédiaire\n3 : Difficile\n")

        match choix_user:
            case "1":
                self.niveau = 1
                return self.niveau

            case "2":
                self.niveau = 2
                return self.niveau

            case "3":
                self.niveau = 3
                return self.niveau

            case _:
                print("Erreur, vous devez taper 1, 2 ou 3")
                return self.__init__()

    def update(self, cible, attaquant):
        if cible.vie <= 0:
            print(f"{cible.nom} est mort(e) ! {attaquant.nom} a gagné !")
            return True
        else:
            return
        
    def lancer_jeu(self):
        if self.niveau == 1:
            joueur = Personnage("Jérome", 60, 20)   
            monstre = Personnage("Chauve-souris", 30, 10)

        elif self.niveau == 2:
            joueur = Personnage("Jérome", 50, 20)
            monstre = Personnage("Gobelin", 40, 20)

        else:
            joueur = Personnage("Jérome", 35, 15)
            monstre = Personnage("Dragon", 80, 30)

        running = True
        tour = "1"
        while running:
            if tour == "1":
                joueur.attaquer(monstre)
                tour = "2"
                if self.update(monstre, joueur):
                    running = False
            else:
                monstre.attaquer(joueur)
                tour = "1"
                if self.update(joueur, monstre):
                    running = False
            
lancer = Jeu()