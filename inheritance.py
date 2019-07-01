class Zwierze:

    def __init__(self, name):
        self.name = name

    def przedstaw_sie(self):
        print(f"Jestem {self.name}")

    def daj_glos(self):
        print("Nie wiem czym jestem i jaki glos wydaje")

class Pies(Zwierze): # w nawiasie podaje po jakiej klasie dziedzicze

    def daj_glos(self):
        print("Hau hau")

# z = Zwierze("niewiadomo co")
# z.przedstaw_sie()
# z.daj_glos()
p = Pies("Burek")
p.przedstaw_sie()
p.daj_glos()

#ex61_inheritance.py
