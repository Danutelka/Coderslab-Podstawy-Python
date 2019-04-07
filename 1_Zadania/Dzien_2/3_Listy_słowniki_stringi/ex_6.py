def message(slownik):
    napis = "In %(movie)s, %(name)s is a %(role)s" %slownik
    return napis


slownik = {
    "name": "Kasia",
    "role": "pirat",
    "movie": "Film"
}


print(message(slownik))

if slownik.get('name') and slownik.get('movie') and slownik.get('role'):
    return "In %(movie)s, %(name)s is a %(role)s" %slownik
else:
    return "None"