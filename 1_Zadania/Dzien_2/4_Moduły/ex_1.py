import random
from random import randint

def d6(num):
    suma = 0
    for _ in range(num):
        suma += random.randint(1, 6)
    return suma

num = 6

print(d6(num))
