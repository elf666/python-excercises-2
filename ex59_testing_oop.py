# stworz klase CutString, oraz dwie metody (dzialajce na instancji klasy):
# 1. zwraca pierwsze 5 znakow stringa (lub mniej, jesli jest krotszy)
# 2. zwraca ostatnie 5 znakow stringa (lub mniej, jesli jest krotszy)
#
# napisz testy do tych metod (po dwie na metode, jakie?)
# uruchom testy

class CutString:

    def __init__(self, string):
        self.string = string

    def return_first_5_chars(self):
        return self.string[:5]

    def return_last_5_chars(self):
        return self.string[-5:]


def test_return_first_5_chars_long_string():
    cs = CutString('123456789')
    assert cs.return_first_5_chars() == '12345'

def test_return_last_5_chars_long_string():
    cs = CutString('123456789')
    assert cs.return_last_5_chars() == '56789'

def test_return_last_5_chars_short_string():
    cs = CutString('123')
    assert cs.return_last_5_chars() == '123'

def test_return_first_5_chars_short_string():
    cs = CutString('123')
    assert cs.return_first_5_chars() == '123'






# class CutString:
#
#     def return_first_5_chars(self, string):
#         return string[:5]
#
#     def return_last_5_chars(self, string):
#         return string[-5:]
#
# cs = CutString()
#
# def test_return_first_5_chars_long():
#     assert cs.return_first_5_chars('12345678') == '12345'
#
# def test_return_first_5_chars_short():
#     assert cs.return_first_5_chars('123') == '123'
#
# def test_return_last_5_chars_long():
#     assert cs.return_last_5_chars('12345678') == '45678'
#
# def test_return_last_5_chars_short():
#     assert cs.return_last_5_chars('123') == '123'
