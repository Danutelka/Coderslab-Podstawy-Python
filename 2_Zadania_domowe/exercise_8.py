def fiber(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    else:
        return fiber(n - 1) + fiber(n - 2)

n = int(input("Podaj wartość n: "))

print(fiber(n))


def fib(n):
    f1 = 1
    f0 = 0
    f2 = f0 + f1
    for i in range(n-2):
        f0 = f1
        f1 = f2
        f2 += f1 +f0
    return f2

print(fib(3))
