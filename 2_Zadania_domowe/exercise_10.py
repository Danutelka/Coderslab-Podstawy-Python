def find_first_and_last(a):
  s =[]
  for i in range(2):
      s += [a[0], a[-1]]
      return s

a = [2, 4, 5, 3, 8, 13]

krotka = tuple(find_first_and_last(a))

print(krotka)

