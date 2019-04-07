def div(n,m):
    try:
        s = n / m
    except ZeroDivisionError:
        print("nie dzielimy przez zero")
    except ValueError:
        print("miala byc liczba!")
    return s

n = int(input("podaj pierwsza liczbe: "))
m = int(input("podaj druga liczbe: "))

wynik = div(n, m)
print(wynik)


