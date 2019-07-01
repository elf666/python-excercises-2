# metoda specjalna __init__ sluzy do konstruowania obiektu

class Dog:

    def __init__(self, name, age, is_barking):
        self.name = name
        self.age = age
        self.is_barking = is_barking

    def print_data_about_dog(self):  # nie musimy podawac argumentow!
        barking_info = ''
        if self.is_barking:
            barking_info = "is barking"
        else:
            barking_info = "is not barking"
        print(f"Dog name is {self.name}, it is {self.age} years old and it {barking_info}.")


burek = Dog("Burek", 5, True)
azor = Dog("Azor", 12, False)
burek.print_data_about_dog()
azor.print_data_about_dog()

# ex52_init.py
