def is_divided_4(x):
    return x % 4 == 0


liczba = int(input("Podaj liczbę: "))
wynik = is_divided_4(liczba)

print(wynik)