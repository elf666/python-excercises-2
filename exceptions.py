# rzucanie (generowanie) wyjatkow
# przyczyna moze byc niedozwolona operacja, np dzielenie przez zero
# mozemy tez sami "rzucic" wyjatkiem


# print(1/0) # ZeroDivisionError
# print(a) # NameError
# A = [1,2,3]
# print(A[3]) # IndexError

#ValueError - dobry typ, zla wartosc
def dodaj_liczby_dodatnie(a,b):
    if a < 0 or b < 0:
        raise ValueError("Ta funkcja nie obsluguje wartosci ujemnych")
    return a + b

# print(dodaj_liczby_dodatnie(-1,2))

#TypeError - zly typ
# def dodaj_dwa_stringi(a,b):
#     if type(a) is not str or type(b) is not str:
        # raise TypeError("Mialy byc stringi!")
#     print(a + b)
#
# dodaj_dwa_stringi(1, 'b c d')

#ex63.py
#ex64.py

# dodaj_liczby_dodatnie(2,3)
# # dodaj_liczby_dodatnie(-2,3)
# dodaj_dwa_stringi("Ala ", "ma kota")

# lapanie wyjatkow
# mozemy sprobowac zlapac i obsluzyc wyjatek tak, aby nie konczyl dzialania programu bledem

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Nie wolno dzielic przez zero!")
#
# print("ale dzialam dalej")

# try:
#     dodaj_liczby_dodatnie(2, -3)
# except ValueError:
#     print("Mialy byc dodatnie, sprobuj jeszcze raz!")

# mozemy uzywac wielu blokow except:

# try:
#     dodaj_liczby_dodatnie(-2,3)
# except TypeError:
#     print("Podales zly typ danych")
# except ValueError:
#     print("Mialy byc dodatnie!")

#ex65.py

# as - dostanie sie do wyjatku

# try:
#     1/0
# except ZeroDivisionError as wyjatek:
#     print("Nie wolno dzielic przez zero!")
#     print(f"Dokladny wyjatek to: {wyjatek}")


# raise - rzucenie wyjatku dalej przez sekcje except:

# try:
#     print(abcd)
# except ZeroDivisionError:
#     print("Nie wolno dzielic przez zero, i co teraz?")
# except:
#     print("Nie wiem co sie stalo :(")
#     raise

#finally - co ma sie wykonac po wystapieniu wyjatku

# try:
#     print(a)
# except NameError:
#     print("Wyglada na to ze taka zmienna nie istnieje")
# finally:
#     "Sprobuj jeszcze raz podajac poprawne dane"
    #czesto tu zamyka sie plik, zamyka polaczenie z baza itp

#ex66.py

# definiowanie wlasnych wyjatkow
# tworzymy klase WlasnyWyjatek dziedziczaca z Exception

class FunkcjaNieTolerujePsow(Exception):
    pass

def print_animal(animal):
    if animal == 'pies':
        raise FunkcjaNieTolerujePsow("Wprowadz inne zwierze niz pies.")
    else:
        print(animal)

print_animal("kot")
print_animal("pies")

# ex67.py


#https://www.tutorialsteacher.com/python/error-types-in-python
