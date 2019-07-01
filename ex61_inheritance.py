# stworz klase HotelGuest, dodaj do niej metody:
# zakwateruj - informuje ze gosc zostal zakwaterowany
# wykwateruj - informuje, ze gosc zostal wykwaterowany
#
# stworz klase PremiumHotelGuest dziedziczaca z HotelGuest, dodaj do niej metody:
# podaj_sniadanie - informuje ze podano sniadanie do lozka
# dostarcz_szampana - informuje, ze dostarczono szampana do pokoju
#
# stworz obiekt klasy PremiumHotelGuest
# zakwateruj go, podaj sniadanie, podaj szampana, wykwateruj
#
# stworz obiekt klasy HotelGuest i sprobuj mu podac szampana. zobacz co sie stanie

class HotelGuest:

    def zakwateruj(self):
        print("Gosc zostal zakwaterowany")

    def wykwateruj(self):
        print("Gosc zostal wykwaterowany")

class PremiumHotelGuest(HotelGuest):

    def podaj_sniadanie(self):
        print("Podano sniadanie")

    def dostarcz_szampana(self):
        print("Dostarczono szampana")

premium_guest = PremiumHotelGuest()
premium_guest.zakwateruj()
premium_guest.podaj_sniadanie()
premium_guest.dostarcz_szampana()
premium_guest.wykwateruj()

regular_guest = HotelGuest()
regular_guest.dostarcz_szampana()






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
#     def podaj_sniadanie(self):
#         print("Podajemy sniadanie")
#
#     def dostarcz_szampana(self):
#         print("A oto szampan dla szanownego pana")
#
# premium_guest = PremiumHotelGuest()
# premium_guest.zakwateruj()
# premium_guest.podaj_sniadanie()
# premium_guest.dostarcz_szampana()
# premium_guest.wykwateruj()
#
# regular_guest = HotelGuest()
# regular_guest.dostarcz_szampana()
