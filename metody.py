class Dog:

    def bark(self):          # metoda bezparametrowa, tylko parametr self
        print("Hau hau!")

    def bite(self, person):  # metoda z parametrem
        print(f"Zaraz ugryze {person}")

burek = Dog()
burek.bark()
burek.bite("Listonosza")
burek.bite("Akwizytora")


#ex51_metody.py
