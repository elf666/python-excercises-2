# stworz klase statyczna ManipulateString ktora posiada dwie metody:
# 1. metoda ktora zmienia stringa na duze litery
# 2. metoda ktora dopisuje na poczatku i koncu stringa * i zmienia go na duze litery
# (korzystajac z metody 1)
# uzyj dekoratorow @staticmethod i @classmethod
# ma dzialac bez instancji!

class ManipulateString:

    @staticmethod
    def upper_string(string):
        return string.upper()

    @classmethod
    def upper_and_add_stars(cls, string):
        uppered = cls.upper_string(string)
        return '*' + uppered + '*'

print(ManipulateString.upper_and_add_stars('papuga'))







# class ManipulateString:
#
#     @staticmethod
#     def make_upper(string):
#         return string.upper()
#
#     @classmethod
#     def add_stars_and_make_upper(cls, string):
#         return '*' + cls.make_upper(string) + '*'
#
# print(ManipulateString.add_stars_and_make_upper('kotek'))
