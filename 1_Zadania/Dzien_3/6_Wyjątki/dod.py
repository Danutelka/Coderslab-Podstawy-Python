def decorate(func):
    def wrapper():
        l=[]
        while True:
            x = func()
            print(x)
            if x != 'k':
                l.append(x)
            else:
                break
        return l
    return wrapper

@decorate
def my_input():
    try:
        x = input('podaj liczbe')
        x = int(x)
    except ValueError:
        x = 'k'
    return x

my_input()