def max_length(d):
    return [i for i in d if len(i) > 5]

d = ["Litwo", "ojczyzno", "moja", "ty", "jestes", "jak", "zdrowie"]
wynik = max_length(d)

print(wynik)
