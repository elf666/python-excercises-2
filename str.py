# class Dog:
#
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return f"Obiekt klasy Dog, name = {self.name}"
#
# b = Dog("Burek")
# print(b)


# metoda specjalna __str__ sluzy do generowania informacji na temat obiektu
# wspolpracuje z funkcja print

class Vector:

    def __init__(self, a, b): # nazwy parametrow w konstruktore nie musza byc identyczne
        self.x = a            # z nazwami pol klasy
        self.y = b
        print(f"Wektor o wspolrzednych: x: {self.x}, y: {self.y} zostal stworzony.")

    def __str__(self):
        return f"Wektor o wspolrzednych x: {self.x}, y: {self.y}"

v1 = Vector(2,3)
print(v1)
v2 = Vector(5,10)
print(v2)

#ex54_str.py
