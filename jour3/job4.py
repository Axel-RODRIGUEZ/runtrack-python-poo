class Joueur:
    def __init__(self, nom, numero, position, nbr_but, nbr_passed, nbr_cartonr, nbr_cartonj):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nbr_but = nbr_but
        self.nbr_passed = nbr_passed
        self.cartonr = nbr_cartonr
        self.cartonj = nbr_cartonj

    def marquer_but(self):
        self.nbr_but += 1
    
    def passe_d(self):
        self.nbr_passed += 1

    def carton_j(self):
        self.cartonj += 1

    def carton_r(self):
        self.cartonr += 1

    def get_infos(self):
        return f"--- INFO JOUEUR ---\nNom : {self.nom}\nNuméro : {self.numero}\nPosition : {self.position}\nNombre de but marqué : {self.nbr_but}\nNombre de passe décisive : {self.nbr_passed}\nNombre de carton rouge : {self.cartonr}\nNombre de carton jaune : {self.cartonj}"

class EquipeDeFoot:
    def __init__(self, nom):
        self.nom = nom
        self.liste = []

    def ajouter_joueur(self, joueur:object):
        self.liste.append(joueur)

    def get_infos(self):
        joueurs = ""

        for joueur in self.liste:

            joueur + f"--- INFO JOUEUR ---\nNom : {self.nom}\nNuméro : {self.numero}\nPosition : {self.position}\nNombre de but marqué : {self.nbr_but}\nNombre de passe décisive : {self.nbr_passed}\nNombre de carton rouge : {self.cartonr}\nNombre de carton jaune : {self.cartonj}\n\n"
        
        return joueurs
    
equipe = EquipeDeFoot("Test")

joueur1 = Joueur("Test1", 2, "Défenseur", 0, 1, 0, 3)
joueur2 = Joueur("Test2", 10, "Attaquant", 3, 2, 1, 1)
joueur3 = Joueur("Test3", 11, "Milieu Offensif", 1, 3, 0, 1)

equipe.ajouter_joueur(joueur1)
equipe.ajouter_joueur(joueur2)
equipe.ajouter_joueur(joueur3)