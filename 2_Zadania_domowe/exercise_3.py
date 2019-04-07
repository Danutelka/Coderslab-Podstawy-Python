def circle_circuit(r, pi = 3.14):
    obwod = (2 * pi) + r
    return obwod

r = int(input("Podaj średnicę okręgu: "))

print(circle_circuit(r, pi = 3.14))