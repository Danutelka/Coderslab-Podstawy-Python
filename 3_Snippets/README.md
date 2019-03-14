<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">


# Podstawy programowania w Pythonie
> Kilka ważnych informacji


Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki:

#### Jak pobrać wartość z klawiatury i przypisać ją do zmiennej?

```python
a = input("Input someting: ")
print(a)  # Wyświetl wartość zmiennej a
```

#### Jak znaleźć część całkowitą liczby zmiennoprzecinkowej i jak zamienić łańcuch tekstowy na liczbę?

```python
a = 100 / 33
print(int(a))  # Wyświetl część całkowitą

b = "2017"
year = int(b)
print("The year is", year)
```

#### Jak stworzyć zestaw liczb od 0 do 10?

```python
a = range(0, 11)
```

#### Jak wylosować liczbę od 10 do 20?

```python
from random import randint

rnd = randint(10, 20)
``` 

#### Jak rozbić łańcuch tekstowy na listę?
```python
my_str = "A long time ago, in a galaxy far, far away..."
my_list = my_str.split()
```

#### Jak połączyć listę słów w jeden łańcuch tekstowy?
```python
my_list = ['A', 'long', 'time', 'ago,', 'in', 'a', 'galaxy', 'far,', 'far', 'away...']
my_str = " ".join(my_list)
```

**Zobacz, co się stanie, gdy zamiast spacji, dasz inny znak w łączeniu tablicy!**

#### Jak zamienić napis z małych na wielkie litery?
```python
txt = "a new hope"
txt2 = txt.upper()
txt3 = "empire strikes back".upper()
print(txt2, txt3)
```
```
'A NEW HOPE EMPIRE STRIKES BACK'
```

#### Jak stworzyć listę liczb z danego zakresu?
```python
a = range(0, 10)
b = list(a)
```

#### Jak wylosować trzy różne liczby z zakresu?
```python
from random import shuffle

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
shuffle(a)
print(a[:3])
```
