# stworz klase Shop
# stworz pole ze zbiorem wszystkich produktow, na poczatku pustym (set)
# stworz pole slownika przechowujacego liczebnosc produktow
# kluczem bedzie rodzaj produktu: wartoscia ilosc produktu
#
# stworz metode dodajaca okreslona ilosc produktu do sklepu i aktualizujaca jego ilosc
# stworz metode sprzedawania okreslonej ilosci danych produktow
# stworz metode sprawdania stanu magazynowego danego produktu
#
# stworz klase Product majaca pole: name
# stworz kilka roznych produktow



class Product:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Shop:

    def __init__(self):
        self.all_products = set()
        self.products_quantity = dict()

    def add_product(self, product, quantity):
        self.all_products.add(product)
        self.add_to_quantity(product,quantity)

    def sell_product(self, product, quantity):
        self.substract_from_quantity(product, quantity)

    def add_to_quantity(self, product, quantity):
        if product.name not in self.products_quantity.keys():
            self.products_quantity[product.name] = quantity
        else:
            self.products_quantity[product.name] += quantity

    def substract_from_quantity(self,product,quantity):
        current_quantity = self.products_quantity[product.name]
        if current_quantity - quantity >=0:
            self.products_quantity[product.name] -= quantity
        else:
            self.products_quantity[product.name] = 0

    def print_quantity_of_product(self, product):
        print(f"Ilosoc {product} w magazynie to {self.products_quantity[product.name]}")

    def print_quantity_of_all_products(self):
        for key in self.products_quantity:
            print(f"{key}: {self.products_quantity[key]}")


shop = Shop()
lyzka = Product("Lyzka")
widelec = Product("Widelec")
shop.add_product(lyzka, 6)
shop.add_product(widelec, 2)
shop.print_quantity_of_all_products()
shop.sell_product(lyzka,3)
shop.print_quantity_of_all_products()
shop.sell_product(widelec,4)
shop.print_quantity_of_all_products()
