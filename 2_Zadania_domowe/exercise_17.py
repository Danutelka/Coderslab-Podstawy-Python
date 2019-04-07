pesel = '84032606443'

def split(pesel):
    return [char for char in pesel]
lista = split(pesel)
print(lista)

def validate_pesel(lista):
    a = 1 * int(lista[0])
    b = 3 * int(lista[1])
    c = 7 * int(lista[2])
    d = 9 * int(lista[3])
    e = 1 * int(lista[4])
    f = 3 * int(lista[5])
    g = 7 * int(lista[6])
    h = 9 * int(lista[7])
    i = 1 * int(lista[8])
    j = 3 * int(lista[9])
    k = 1 * int(lista[10])
    suma = a + b + c + d + e + f + g + h + i + j
    modulo = (suma % 10)
    kontrola = (10 - modulo)
    if kontrola == k:
        return "pesel poprawny"
    else:
        return "pesel niepoprawny"



print(validate_pesel(lista))
