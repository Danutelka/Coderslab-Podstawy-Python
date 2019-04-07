def phone(number):
    if number in [333, 444, 555, 666]:
        return "Jest"
    else:
        raise Exception("Nie ma takiego numeru")

print(phone(666))