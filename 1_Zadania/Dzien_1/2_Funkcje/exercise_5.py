

def create_name(name, surname, nickname):
    return "{} '{}' {}" .format(name, nickname, surname)

text = create_name("Danuta", "Kawecka", "Danutella")
print (text)