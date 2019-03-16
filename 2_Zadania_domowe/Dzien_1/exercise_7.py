def histogram(tablica):
    s = ""
    for el in tablica:
        if type(el) == int:
         s += "#" * el
         s += " \n"
        else:
            return None
    return s

h = histogram([1, 5, 12, 20])
print(h)
