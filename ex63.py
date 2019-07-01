stworz funkcje ktora pobiera dwa integery i podnosi pierwszy do potegi drugiego
sprawdz czy faktycznie otrzymala integery, jesli nie to rzuc TypeError



a ** b

if type(a) is not int

raise TypeError("tu jakis komentarz")









def power(a,b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("Mialy byc integery!")
    return a ** b

print(power(2.5,5))
