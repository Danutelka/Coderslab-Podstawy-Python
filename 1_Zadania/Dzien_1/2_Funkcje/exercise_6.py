def calculate_net(gross, vat):
    net = gross / (1 + vat)
    return net

def calculate_all(kwota, vat):
    net = calculate_net(kwota, vat)
    print("brutto: %d, netto: %d, vat: %d%%, różnica: %d" % (kwota, net, vat * 100, kwota - net))

kwota = float(input("Podaj kwotę: "))
vat = float(input("Podaj vat: "))


print(calculate_net(kwota, .23))
print(calculate_net(kwota, .08))
print(calculate_net(kwota, .05))
print(calculate_net(kwota, .00))


calculate_all(kwota, vat)