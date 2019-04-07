def list_key(d):
    lista =[]
    for key in d:
        lista.append(key)
    return lista


d = {"kot": 1, "pies": "Milord"}
klucze = list_key(d)

print(klucze)