def find_boundaries(b):
    tab = []
    tab.append(max(b))
    tab.append(min(b))
    return tab

def find_bound2(c):
    tab2 =[]

    tab2.append(max(c))
    tab2.append(max(c))
    return tab2

b = [1, 5, 2, 3.5, -1]
c = [1, 'cos', 2, 3]

krotka = tuple(find_boundaries(b))

print(krotka)

print(find_bound2(c))


