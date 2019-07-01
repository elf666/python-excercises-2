# stworz klase Telefon, ktora posiada metode dzwon
# stworz klase Aparat, ktora posiada metode rob_zdjecia
# stworz klase Mapa, ktora posiada metode znajdz_droge
# kazda z tych klas ma rowniez posiadac metode przedstawienia sie (Jestem telefon...)
#
# stworz klase Smartfon, ktora dziedziczy z trzech powyzszych klas
# stworz w niej metode uzyj_facebooka
#
# stworz obiekt klasy Smartfon i wywolaj na nim metody:
# przedstaw_sie, dzwon, rob_zdjecia, znajdz_droge i uzyj_facebooka
#
# nadpisz metode przedstaw_sie, tak aby smartfon przedstawial sie poprawnie


class Telefon:
    def przedstaw_sie(self):
        print("Jestem telefonem")

    def dzwon(self):
        print("Dzwonie")

class Aparat:
    def przedstaw_sie(self):
        print("Jestem aparatem")

    def rob_zdjecia(self):
        print("Robie zdjecia")

class Mapa:
    def przedstaw_sie(self):
        print("Jestem mapa")

    def znajdz_droge(self):
        print("Znajduje droge")

class Smartfon(Mapa, Aparat, Telefon):

    def uzyj_facebooka(self):
        print("Uzywam facebooka")

    def przedstaw_sie(self):
        print("Jestem smartfonem")

s = Smartfon()
s.przedstaw_sie()
s.dzwon()
s.rob_zdjecia()
s.znajdz_droge()
s.uzyj_facebooka()
