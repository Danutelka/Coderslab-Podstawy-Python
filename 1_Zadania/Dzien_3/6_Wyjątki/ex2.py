def divide(a,b):
    try:
        int(a)
        int(b)
        return True
    except ValueError:
        return None

a = 5
b = "dddd"

print(divide(a,b))
