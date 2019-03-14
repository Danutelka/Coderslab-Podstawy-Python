<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">


# Podstawy programowania w Pythonie - zadania domowe
> Wszystkie zadania rozwiązuj w funkcjach. 
> Jeśli Twoje funkcje nie będą zwracały wartości nie będą zaliczone (chyba, że jest napisane, żeby nie wykonywać działanie w funkcji). Każde zadanie rozwiązuj w oddzielnym pliku (np. zadanie 1. w pliku exercise_1.py, zadanie 2. w pliku exercise_2.py itd.)
> Możesz wypisywać w konsoli informacje, ale **nie myl tego ze zwracaniem wartości**.
> 
> Zadania z gwiazdką __(*)__ są dla chętnych
>
> Czytaj uważnie polecenia.


# Dzień 1.

#### Zadanie 0.

Zapoznaj się z **PEP-8**. Jest to oficjalny dokument opisujący styl kodowania w Pythonie:

https://www.python.org/dev/peps/pep-0008/

Wracaj do niego regularnie wraz z postępem nauki i staraj się stosować do podanych tam wytycznych. 

#### Zadanie 1 

(W tym zadaniu nie musisz pisać funkcji)

Napisz program, w którym zdefiniujesz wielolinijkowy łańcuch tekstowy. Wpisz tam zwrotkę swojego ulubionego wiersza, po czym wyświetl go na konsoli.

#### Zadanie 2

Napisz funkcję o nazwie `square_area` która policzy i **zwróci** pole prostokąta (przyjmując dwa parametry oznaczające długość jego boków). Przyjmij, że parametry wejściowe są poprawne.

#### Zadanie 3

Napisz funkcję o nazwie `circle_circuit`, która przyjmując średnicę okręgu **zwróci** jego obwód. Przyjmij, że parametry wejściowe są poprawne. Przyjmij `pi=3.14`.

#### Zadanie 4
 
Napisz funkcję o nazwie `dogs_age`, który przeliczy wiek psa w psich latach. 

* funkcja powinna przyjmować wiek psa jako parametr,
* dla pierwszych dwóch lat, każdy rok życia psa jest równy 10.5 ludzkiego roku,
* powyżej dwóch lat, każdy rok życia psa, to 4 ludzkie lata,
* funkcja powinna **zwrócić** wiek psa.

##### Przykład:
```python
azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75

burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33
```

#### Zadanie 5.

Napisz funkcję `chessboard`, który przyjmie parametr `n` jako opcjonalny. Standardowa wartość parametru ma wynosić 8. Funkcja ma **zwrócić** wielolinijkowy napis reprezentujący szachownicę złożoną ze znaków # i spacji. Szachownica powinna mieć wymiary **n x n**. 

**Przykład:**
Przy n=8, szachownica powinna składać się 8 wierszy, każdy po 8 znaków, naprzemiennie # i spacja.
```python
c = chessboard()
print(c)
```
```
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # # 
```

#### Zadanie 6.

Napisz funkcję `is_divided_by_4`, która przyjmie liczbę i sprawdzi, czy liczba jest podzielna przez 4 i odpowiednio zwróci `True` lub `False`.

#### Zadanie 7.

Napisz funkcję `histogram`, która przyjmie listę liczb, po czym **zwróci** histogram ze znaków `#`. Jeśli użytkownik poda wartość nie będącą liczbą, funkcja powinna zwrócić wartość `None`.

Wynikowy histogram ma być wielolinijkowym napisem składającym się ze znaków `#`. Jedna linijka = jeden słupek histogramu.

##### Przykład:
```python
h = histogram([2, 6, 3, 1])
print(h)
```
```
##
######
###
#
```

```python
h = histogram([1, 2, 'error!'])
print(h)
```
```
None
```

#### Zadanie 8(\*). Ciąg Fibonacciego.

Napisz funkcję `fib` liczącą ciąg Fibonacciego. Funkcja powinna:

* przyjmować jako parametr `n` - liczbę; ma to być element, dla którego liczymy wartość,
* zwracać wartość elementu ciągu dla elementu `n`.

##### Podpowiedź:

Ciąg Fibonacciego to ciąg liczb naturalnych. Określa się go rekurencyjnie w sposób następujący: pierwszy element jest równy 0, drugi 1, każdy następny jest sumą dwóch poprzednich.

Sprawdź w internecie, co to jest _rekurencja_ i jak napisać funkcję, która to wykorzystuje.


# Dzień 2.

#### Zadanie 9.

Napisz funkcję `make_tuple`, która przyjmie cztery parametry: `a`, `b`, `c` i `d`. Niech parametry `c` i `d` bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4. Zwróć krotkę czterech elementów, której kolejnymi elementami będą wartości parametrów.

##### Przykład:

```python
a = make_tuple("mama", "tata")
print(a)
```
```
('mama', 'tata', 3, 4)
```
```python
a = make_tuple(0, 0, 0, 0)
print(a)
```
```
(0, 0, 0, 0)
```

#### Zadanie 10.

Napisz funkcję `find_first_and_last`, która przyjmie listę lub krotkę. Następnie zwróć krotkę, która będzie zawierać pierwszy i ostatni element parametru.

#### Zadanie 11.

Napisz funkcję `format_date`, która przyjmie 3 parametry:

* `day`: dzień,
* `month`: miesiąc,
* `year`: rok.

Funkcja powinna sprawdzić, czy data jest poprawna: 
* miesiąc powinen być w granicach (1, 12),
* dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).

Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić `None`.  

Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".

##### Przykład

```python
d = format_date(12, 1, 2017)
print(d)
```
```
12 stycznia 2017
```
```python
d = format_date(12, 13, 2017)
print(d)
```
```
None
```

#### Zadanie 12.

Napisz funkcję `find_boundaries`, która przyjmie listę liczb. Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie. Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany. W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić `None`.

##### Przykład:
```python
b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
```
```
(-1, 5)
```
```python
b = find_boundaries([0, 2, "a kuku!", 10])
print(b)
```
```
(0, 10)
```

#### Zadanie 13.

Napisz funkcję `censor`, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:

* rozbije łańcuch tekstowy na listę wyrazów,
* sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
* jeśli tak -- zamieni je na cztery gwiazdki (`****`)
* ponownie połączy listę w string i zwróci wartość.

##### Słowa niedozwolone:
*Java*, *C#*, *Ruby*, *PHP*. 
(zwróć uwagę na wielkość znaków np. 'PhP' **nie** powinno być ocenzurowane)

Słowa niedozwolone trzymaj jako listę wewnątrz funkcji `censor`.

##### Przykład
```python
c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)
```
```
**** is the best, but **** is the bestest!
```

#### Zadanie 14.

Napisz funkcję `check_palindrome`, która pobierze jeden wyraz i sprawdzi, czy jest palindromem. Funkcja powinna zwracać `True`, jeśli łańcuch jest palindromem, `False`, jeśli nie jest.

# Dzień 3.

#### Zadanie 15.

Napisz funkcję `random_average(n)`, która wylosuje `n` liczb naturalnych od 1 do 100, zsumuje je, po czym zwróci średnią arytmetyczną z tych liczb.

Ze względu na konstrukcję testów automatycznych użyj w zadaniu poniżeszj formy importu funkcji `randint`:

```python
import random
```

a następnie w kodzie używaj konstrukcji:

```python
random.randint()
```

#### Zadanie 16.

Napisz funkcję `div`, która:

* poprosi użytkownika o podanie 2 liczb z klawiatury,
* wprowadzone dane zamieni na liczby naturalne,
* podzieli jedną liczbę przez drugą,
* wyświetli wynik.

Dodatkowo należy zabezpieczyć się przed wszystkimi możliwymi błędami (niewłaściwe dane, dzielenie przez zero). 

Sprawdź w interaktywnej konsoli Pythona, jakie błędy mogą wystąpić i zabezpiecz się przed nimi.

---
#### Zadanie 17(*): Sprawdzanie poprawności numeru PESEL.

Napisz funkcję `validate_pesel`, która przyjmie numer PESEL jako łańcuch tekstowy, po czym sprawdzi jego poprawność i zwróci:

* `True`, jeśli PESEL jest poprawny,
* `False`, jeśli PESEL jest błędny.

##### Zasady walidacji numeru PESEL

PESEL składa się z 11 cyfr, z czego ostatnia jest cyfrą kontrolną. Aby sprawdzić PESEL, należy:

* pierwsze dziesięć cyfr pomnożyć przez odpowiednią _wagę_, 
* otrzymane iloczyny zsumować,
* sumę podzielić modulo 10,
* wynik dodawania odjąć od 10, jeśli wynik będzie wynosił 10, należy wziąć 0.

Jeżeli wynik powyższej operacji będzie równy ostatniej cyfrze numeru PESEL, cały numer jest poprawny.

##### Wagi:

`1 3 7 9 1 3 7 9 1 3`


##### Przykład:
Chcemy sprawdzić PESEL 44051401358. Zgodnie z procedurą, sprawdzamy dziesięć pierwszych cyfr, ostatnia (8) jest cyfrą kontrolną.

|         |   |    |   |    |   |    |   |   |   |    |
|---------|---|----|---|----|---|----|---|---|---|----|
| **cyfra**   | 4 | 4  | 0 | 5  | 1 | 4  | 0 | 1 | 3 | 5  | 
| **waga**  | 1 | 3  | 7 | 9  | 1 | 3  | 7 | 9 | 1 | 3  |
| **iloczyn** | 4 | 12 | 0 | 45 | 1 | 12 | 0 | 9 | 3 | 15 |

Sumujemy iloczyny: 4 + 12 + 0 + 45 + 1 + 12 + 0 + 9 + 3 + 15 = **101**

Sumę dzielimy modulo 10: 101 % 10 = **1**

Wynik dzielenia modulo odejumemy od 10: 10 - 1 = **9**.

Podana w PESEL-u cyfra kontrolna wynosi **8**, zatem PESEL jest błędny.

# Dzień 4

#### Zadanie 18.
Napisz aplikację Flask, która poprosi użytkownika o wpisanie liczby naturalnej `n` (na akcji GET "/"), a potem (na akcji POST "/") wyświetli tabelkę zawierającą w kolejnych wierszach:

* 2 do potęgi n
* n do potęgi n
* n silnia

Liczbę wysyłaj jako parametr `n`.

**Wskazówka: Pamiętaj o wyświetleniu guzika do wysłania formularza!**

#### Zadanie 19.
Napisz aplikację Flaska, która poprosi użytkownika o wpisanie kodu pocztowego (na akcji GET "/"), a potem (na akcji POST "/") wyświetli informację:

* `Kod poprawny`, jeżeli kod jest w poprawnym polskim formacie (00-001).
* `Kod niepoprawny`, w przeciwnym wypadku

Kod wysyłaj jako parametr `code`.

**Wskazówka: możesz rozbić podany ciąg znaków po myślniku i sprawdzić czy obie części spełniają warunki.**

**Wskazówka: Pamiętaj o wyświetleniu guzika do wysłania formularza!**
