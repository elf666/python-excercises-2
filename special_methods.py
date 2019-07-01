# lista metod specjalnych, ktore mozemy nadpisac
# https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/

class StrangeNumber:

    def __init__(self, number):
        self.strange_number = number

    def __add__(self, other):
        return f"*{str(self.strange_number)}{str(other.strange_number)}*"

sn1 = StrangeNumber(5)
sn2 = StrangeNumber(8)

print(sn1 + sn2) # sn1.__add__(sn2)
