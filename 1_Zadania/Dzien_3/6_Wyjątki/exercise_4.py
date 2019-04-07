from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Podaj liczbę:")
    try:
        num = int(str_num)
        if num == rnd:
            print("Brawo!")
            guessed = True
        elif num >= (rnd-1) and num <= (rnd+1):
            print("cieplej")
        elif num >= (rnd-2) and num <= (rnd+2):
            print("zimno")
        else:
            print("Pudło!")
    except ValueError:
        print("jeszcze raz to nie liczba")


