class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        

burek = Dog('Burek', 'kundelek')
azor = Dog('Azor', 'owczarek niemiecki')

print(burek.name, burek.breed)
print(azor.name, azor.breed)
