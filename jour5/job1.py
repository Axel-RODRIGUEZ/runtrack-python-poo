class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"Nom de l'objet : {self.name}\nMatériel utilisé : {self.material}"
    
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        for part in self.__parts.values():
            print(f"- {part}")

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part

    def change_part(self, part_name, new_material):
        part_a_modifier = self.__parts.get(part_name)
        if part_a_modifier:
            part_a_modifier.material = new_material

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale du {self.name} : {self.max_speed} nœuds")