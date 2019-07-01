# stworz funkcje ktora pobiera tylko stringi zapiane malymi literami
# jesli przekazana wartosc nie jest stringiem rzuc TypeError
# jesli przekazany string nie jest malymi literami rzuc ValueError
# jesli string jest ok, to wydrukuj go
#
# napisz blok try/except w ktorym probujesz uruchomic ta funkcje
# zlap oba mozliwe wyjatki i poinformuj usera o tym co poszlo nie tak

def reprint(string):
    if type(string) is not str:
        raise TypeError("Mial byc string!")
    if not string.islower():
        raise ValueError("String mial byc malymi literami")
    print(string)


try:
    reprint(True)
except TypeError:
    print("Podales zly typ danych")
except ValueError:
    print("Podales dobry typ danych ale zla wartosc (jest jakas duza litera)")
