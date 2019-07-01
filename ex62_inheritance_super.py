# skopiuj klase HotelGuest z poprzedniego zadania
# stworz klase PremiumHotelGuest dziedziczaca z HotelGuest
# nadpisz i przy uzyciu metody super() zmodyfikuj medoty zakwateruj i wykwateruj
# tak aby przed i po informacji jakie one drukuje pojawily sie formulki grzecznosciowe
#
# stworz obiekt klasy PremiumHotelGuest, zakwateruj i wykwateruj go
# prownaj z dzialaniem dla obiektu klasy HotelGuest

class HotelGuest:

    def __init__(self, name):
        self.name = name

    def zakwateruj(self):
        print(f"Gosc {self.name} zostal zakwaterowany")

    def wykwateruj(self):
        print("Gosc zostal wykwaterowany")

class PremiumHotelGuest(HotelGuest):

    def zakwateruj(self):
        print(f"Dzien dobry {self.name}")
        super().zakwateruj()
        print("Serdecznie witamy")

    def wykwateruj(self):
        print("Dzien dobry")
        super().zakwateruj()
        print("Serdecznie zegnamy")

phg = PremiumHotelGuest("Stefan")
phg.zakwateruj()
phg.wykwateruj()
# print("***")
# hg = HotelGuest()
# hg.zakwateruj()
# hg.wykwateruj()










# class HotelGuest:
#
#     def zakwateruj(self):
#         print("Zakwaterowano")
#
#     def wykwateruj(self):
#         print("Wykwaterowano")
#
# class PremiumHotelGuest(HotelGuest):
#
#     def zakwateruj(self):
#         print("Dzien dobry")
#         super().zakwateruj()
#         print("Szanownego pana")
#
#     def wykwateruj(self):
#         print("Do widzenia")
#         super().wykwateruj()
#         print("Szanownego pana")
#
#
# lord_vader = PremiumHotelGuest()
# lord_vader.zakwateruj()
# lord_vader.wykwateruj()
