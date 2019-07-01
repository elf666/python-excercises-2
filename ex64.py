# stworz funkcje ktora pobiera stringa i zamienia go na liste
# funkcja ma pracowac tylko na stringach napisanych malymi literami
# jesli dostanie inny string powinna rzucic ValueError z odpowiednim komentarzem



def make_list_of_string(string):
    if not string.islower():
        raise ValueError("String mial sie skladac z malych liter")
    return list(string)

print(make_list_of_string('abcd'))
