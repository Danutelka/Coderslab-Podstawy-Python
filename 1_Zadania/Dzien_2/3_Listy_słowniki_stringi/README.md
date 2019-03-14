<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Listy, słowniki, stringi

#### Zadanie 1 - rozwiązywane z wykładowcą

Napisz funkcję `create_list`, która przyjmie dwa argumenty dowolnego typu, a następnie zwróci listę, której kolejne elementy będą parametrami powtórzonymi czterokrotnie.

##### Przykład:

```python
my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]
```

#### Zadanie 2 - rozwiązywane z wykładowcą

Napisz funkcję `list_keys(d)`, gdzie `d` to dowolny słownik. Niech funkcja przeiteruje pętlą **for** po kluczach słownika i zwróci listę tych kluczy. Sprawdź w dokumentacji, czy można zrobić to prościej.

----

#### Zadanie 3.

Napisz funkcję `max_length`, która przyjmie listę wyrazów. Funkcja powinna zwrócić listę słów krótszych od 5 znaków.

##### Przykład
```python
l = max_length(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)
```
```
['moja', 'ty', 'jak']
```

#### Zadanie 4.

Napisz funkcję `sum(numbers)` gdzie `numbers` to lista liczb dowolnego typu. Funkcja powinna zwrócić sumę wszystkichh elementów listy `numbers`.

#### Zadanie 5.

Napisz funkcję `mean(numbers)`, gdzie `numbers` to lista liczb dowolnego typu. Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers. Czy znasz jakiś sposób, by ułatwić sobie pracę?

#### Zadanie 6.

Napisz funkcję `message`, która jako parametr przyjmie słownik o następujących kluczach:

* **name**,
* **role**,
* **movie**.

Następnie niech funkcja przygotuje sformatowany napis: "In _movie_, _name_ is a _role_.", gdzie w odpoweidnie miejsca podstawi wartości z ww. kluczy. Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość `None`.

##### Przykład:

```python
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
```

##### Wynik:
```
In Star Wars, Han Solo is a smuggler.
```
```python
input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
```

##### Wynik:
```
None
```

