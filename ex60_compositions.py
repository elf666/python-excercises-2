# stworz klasy:
# Customer - zawierajaca name oraz email
# Item - zawierajaca name i price
# Order - zawierajaca: order_id, customer i item
# w klasie Order dodaj metode specjalna __str__ do wydrukowania danych zamowienia

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, customer, item):
        self.order_id = order_id
        self.customer = customer
        self.item = item

    def __str__(self):
        return f"Zamowienie nr {self.order_id} zlozone przez {self.customer.name} to {self.item.name}"

c = Customer('Jan Kowalski', 'jasio@gmail.com')
i = Item("gumowa kaczuszka", 10)
my_order = Order(100, c, i)
print(my_order)












# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Order:
#     def __init__(self, id, customer, item):
#         self.id = id
#         self.customer = customer
#         self.item = item
#
#     def __str__(self):
#         order_details = f"Zamowienie o numerze: {self.id}\n" + \
#                         f"Zlozone przez klienta: {self.customer.name}\n" + \
#                         f"Jest na produkt: {self.item.name}\n" + \
#                         f"I kosztowalo: {self.item.price} zlotych."
#         return order_details
#
# c = Customer("Jan Kowalski", "jasio@gmail.com")
# i = Item("Gumowa kaczuszka", 50)
# order1 = Order(101, c, i)
# print(order1)
