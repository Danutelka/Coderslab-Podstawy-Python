def check_palimdrome(a):
    c = a[::-1]
    if a == c:
        print(True)
    else:
        print(False)

a = input("Podaj slowo: ")
b = check_palimdrome(a)

print(b)


