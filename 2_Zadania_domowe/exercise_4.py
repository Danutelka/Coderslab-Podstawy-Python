def dogs_age(wiek):
    if wiek < 2:
        par = 10.5
    else:
        par = 4
    return wiek * par

print("kiedy wiek psa to 3: ", dogs_age(3))
