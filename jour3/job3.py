class ListeDeTache:

    def __init__(self):
        self.taches = []

    def voir_liste(self):
        if self.taches:
            taches = ""
            for tache in self.taches:
                taches += f'{tache.titre} - {tache.desc} | {tache.statut}\n'

            return taches
        else:
            return "Il n'y a aucune tâche présente."
        
    def créer_tache(self):
        titre, desc, statut = input("Choisissez un titre : ").capitalize(), input("Choisissez une description : "), input("Choisissez un statut (à faire / en cours / terminé) : ")
        nouvelle_tache = Tache(titre, desc, statut)
        self.taches.append(nouvelle_tache)
        return f'Tâches {titre} ajouté !'
    
    def supprimer_tache(self):
        print("----- Liste actuelle -----")
        print(self.voir_liste())

        choix_user = input("Quel tâche voulez-vous supprimer (titre) : ").capitalize()

        tache_a_supprimer = None

        for tache in self.taches:
            if choix_user == tache.titre:
                tache_a_supprimer = tache
                break

        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            return f'La tâche {choix_user} a été supprimée.'
        else:
            return 'Aucune tâche trouvée pour ce titre'
        
    def marquer_tache(self):
        print("----- Liste actuelle -----")
        print(self.voir_liste())

        choix_user = input("Quel tâche voulez-vous marquer comme terminée (titre) : ").capitalize()

        for tache in self.taches:
            if choix_user == tache.titre:
                tache.statut = "Terminée"
                return f'La tâche {tache.titre} a bien été marquée comme terminée !'
            else:
                return f"Erreur : La tâche {tache.titre} n'existe pas"
            
    def filtrer_liste(self):
        choix_user = input("Choisissez un statut à filtrer (à faire, en cours, terminée) : ")
        
        taches = ""

        for tache in self.taches:
            if choix_user == tache.statut:
                taches += f'{tache.titre} - {tache.desc} | {tache.statut}\n'
        for tache in self.taches:
            if choix_user == tache.statut:

                return taches
            else:
                return f'Aucune tâche comportant le statut {choix_user} est dans la liste.'

class Tache():

    def __init__(self, titre, desc, statut):
        self.titre = titre
        self.desc = desc
        self.statut = statut

ma_liste = ListeDeTache()

ma_liste.créer_tache()
print(ma_liste.voir_liste())
print(ma_liste.marquer_tache())
print(ma_liste.voir_liste())
print(ma_liste.filtrer_liste())