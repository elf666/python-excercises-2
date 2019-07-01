class Employee:

    def __init__(self, name, surname, years_in_company, income_per_year):
        self.name = name
        self.surname = surname
        self.years_in_company = years_in_company
        self.income_per_year = income_per_year
        self.total_income_so_far = self.calculate_total_income()
        # wolajac inna metode klasy podajemy przed jej nazwa self.


    def calculate_total_income(self):
        return self.income_per_year * self.years_in_company


tadeusz = Employee("Tadeusz", "Kowalski", 5, 100000)

print(tadeusz.name)
print(tadeusz.surname)
print(tadeusz.years_in_company)
print(tadeusz.income_per_year)
print(tadeusz.total_income_so_far)

#ex53_more_init.py
