class Human:

    def __init__(self, name):
        self.name = name

class Pet:

    def __init__(self, name):
        self.name = name

class Roommates:

    def __init__(self, human_roommate, pet_roommate, room_name):
        self.human = human_roommate
        self.pet = pet_roommate
        self.room_name = room_name


    def __str__(self):
        return f"Moi wspollokatorzy to: {self.human.name} oraz zwierze {self.pet.name}"

p = Pet("Papuga")
h = Human("Grzesiek")
roommates = Roommates(h, p, "Pokoj zielony")
print(roommates)

# ex60_compositions.py
