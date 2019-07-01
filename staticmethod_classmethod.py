class SomeClass:

    @staticmethod          # metoda statyczna nie jest swiadoma bycia czescia klasy
    def add_numbers(a,b):  # a wiec nie widzi innych metod tej klasy
        return a + b

    # @staticmethod
    # def multiply_and_add(a,b):
    #     a = a * 2
    #     b = b * 2
    #     return add_numbers(a,b)

    @classmethod                    # metoda klasowa jest swiadoma bycia czescia klasy
    def multiply_and_add(cls,a,b):  # i widzi inne metody w klasie
        a = a * 2                   # wymaga slowa kluczowego cls (zamiast self)
        b = b * 2                   # bo operuje na klasie a nie na jej obiekcie/instancji
        return cls.add_numbers(a,b)


print(SomeClass.add_numbers(5,6))
print(SomeClass.multiply_and_add(5,6))

#ex58.py
