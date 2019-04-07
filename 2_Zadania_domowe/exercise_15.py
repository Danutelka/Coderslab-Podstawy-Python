import random

def random_average(n):
    my_list = []
    suma = 0
    for i in range(n):
        my_list.append(random.randint(0, 101))
    return my_list

n = int(input("Ile liczb chcesz wylosować?: "))

wynik = random_average(n)
suma = 0

for i in range(n):
    dodawanie = suma + wynik[i]

for i in range(n):
    srednia = dodawanie / n

print("wylosowano liczby: {wynik}, Ich suma to: {dodawanie}, a ich srednia: {srednia}" .format(wynik=wynik, dodawanie=dodawanie, srednia=srednia))








