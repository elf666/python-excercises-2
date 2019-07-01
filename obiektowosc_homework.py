ex57_sklep.py
ex66.py

zadanie1
stworz klase Uczen, dodaj jej pola imie, nazwisko, oceny
pole oceny powinno byc slownikiem, w ktorym kluczem jest nazwa przedmiotu a
wartoscia ocena z przedmiotu, np:
oceny = {'matematyka': 5, 'biologia': 3}
stworz metode dodajaca przedmiot do slownika zawierajacego oceny
stworz metode modyfikujaca ocene z podanego przedmiotu
stworz metode specjalna __str__ wypisujaca wszystkie dane o uczniu wraz z jego ocenami

zadanie2
stworz klase Pojazd, ktora posiada pole name i metode ruszaj_sie
metoda ruszaj_sie powinna drukowac ogolna informacje o poruszaniu sie
stworz klasy Samochod, Samolot, Statek ktore dziedzicza z klasy Pojazd
i nadpisuja jej metode ruszaj_sie informujac o swoim specyficznym sposobie poruszania sie
stworz konstruktor dla kazdej z klas dziedziczacych, ktory przy uzyciu metody super()
dziedziczy konstruowanie pola self.name z klasy Pojazd, oraz dodaje drugie pole type

zadanie3
stworz klase ManipulateData, ktora bedize klasa statyczna (jej metody nie beda
pracowac na instancjach)
stworz metody:
increase_number_by(x,y) - zwieksz numer x o y
power(x,y) - ktora podnosi liczbe x do potegi y
print_as_string(some_int) - ktora zamienia integera na strina i drukuje go.

przy uzyciu dekoratora @staticmethod i @classmethod zaimplementuj klase tak,
aby powyzsze metody mogly wywolywac sie nawzajem
uruchom metody print_as_string, ktora bedize wywolywac metode power,
ktora bedize wywolywac metode increase_number_by i przetestuj jej
dzialanie na kilku roznych integerach

zadanie4
na podstawie klasy ManipulateData z zadania3 stworz klase NIESTATYCZNA,
ktora bedize posiadala analogiczne metody (ale dzialal na instancji)
napisz testy, ktore beda testowac metody increase_number_by, power i print_as_string
zaplanuj po kilka testow dla kazdej metody
np dla increase_number_by przetestuj jej dzialanie dla liczb dodatnich i ujemnych
uruchom pytest i sprawdz czy testy przechodza

zadanie5
stworz funckje ktora pobiera stringa i zwraca go odwroconego (kotek -> ketok)
funkcja ma dzialac tylo na stringach krotszych niz 11 znakow
jesli string bedize za dlugi to rzuc wyjatek TooLongString
(w tym celu musisz utworzyc taki wyjatek)
uruchom funkcje przy uzyciu blokow try/except/finally

zadanie6
Stworz klase Szkola, zawieraja pola:
- nazwa szkoly
- lista uczniow
- lista nauczycieli
oraz metody:
- dodaj ucznia, usun ucznia
- dodaj nauczyciela, usun nauczyciela
- wypisz informacje o uczniach, wypisz informacje o nauczycielach

Stworz klase Uczen i klase Nauczyciel
stworz po kilka obiektow uczniow i nauczycieli i dodaj ich do odpowiednich pol klasy szkola
