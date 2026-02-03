class Student:
    def __init__(self, nom, prenom, id_etud):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etud = id_etud
        self.__nbr_credit = 0
        self.__level = self.__student_eval()

    def get_credit(self):
        return self.__nbr_credit
    
    def add_credit(self, nbr_credit):
        if nbr_credit <= 0:
            print("Erreur, veuillez entrer un nombre supérieur à zéro.")

        else: 
            self.__nbr_credit += nbr_credit
    
    def __student_eval(self):
        if self.__nbr_credit >= 90:
            return "Excellent"

        elif self.__nbr_credit >= 80 and self.__nbr_credit <= 89:
            return "Très bien"
        
        elif self.__nbr_credit >= 70 and self.__nbr_credit <= 79:
            return "Bien"
        
        elif self.__nbr_credit >= 60 and self.__nbr_credit <= 69:
            return "Passable"
        
        else: 
            return "Insuffisant"

    def student_info(self):
        print(f"Nom : {self.__nom}\nPrénom : {self.__prenom}\nId : {self.__id_etud}\nNiveau : {self.__level}")
    

student = Student('John', 'Doe', 145)

student.add_credit(20)
student.add_credit(20)
student.add_credit(20)

print(student.get_credit())


student.student_info()