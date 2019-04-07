import datetime


def tommorow():
    dzis = datetime.datetime.now()
    jutro = dzis + datetime.timedelta(days=1)
    return jutro


print(tommorow())