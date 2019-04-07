def sum(numbers):
    suma = 0
    for i in range(len(numbers)):
        suma += numbers[i]
    return suma

numbers = [1, 4, 3, 4, 6, 7]

wynik = sum(numbers)

print(wynik)

def mean(numbers):
    srednia = 0
    for i in range(len(numbers)):
        srednia = float(wynik / numbers[i])
    return srednia

wynik2 = mean(numbers)
print(wynik2)