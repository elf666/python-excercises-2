class SimpleWelcomeClass:

    def welcome_user(self):
        print("Hello user!")

    @staticmethod # informuje ze metoda ponizej jest statyczna
    def welcome_user_without_object():
        print("Hello user! I don't need an object")


# s1 = SimpleWelcomeClass() # tworzenie obiektu
#
# s1.welcome_user()
SimpleWelcomeClass.welcome_user_without_object()
