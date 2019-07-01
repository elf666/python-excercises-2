class ZwierzeLadowe:

    def przedstaw_sie(self):
        print("Jestem zwierzeciem ladowym")

    def idz(self):
        print("Chodze tu i tam")

class ZwierzeMorskie:

    def przedstaw_sie(self):
        print("Jestem zwierzeciem morskim")

    def plywaj(self):
        print("Plywam sobie w kolko")

class SwinkaMorska(ZwierzeLadowe, ZwierzeMorskie):

    def przedstaw_sie(self):
        super().przedstaw_sie()
        # print("Jestem swinka morska")

mariolka = SwinkaMorska()
mariolka.przedstaw_sie()
# mariolka.idz()
# mariolka.plywaj()


#ex62_inheritance_multi.py
