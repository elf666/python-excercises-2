class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class ItEmployee(Employee):

    def __init__(self, name, salary, specialisation):
        super().__init__(name, salary)
        self.specialisation = specialisation

it_guy = ItEmployee("Janusz", 5000, "Naprawia drukarki")
print(it_guy.name, it_guy.salary, it_guy.specialisation)

#ex62_inheritance_super.py
