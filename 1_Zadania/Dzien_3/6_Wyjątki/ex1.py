def safe_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None

l = [1,2,3,4]

print(safe_get(l, 5))
print(safe_get(l, 3))
