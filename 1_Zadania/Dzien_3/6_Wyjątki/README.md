<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Wyjątki

#### Zadanie 1 - rozwiązywane z wykładowcą.

Napisz funkcję `safe_get`, która przyjmue dwa parametry:

* `l`: dowolna lista,
* `index`: liczba.

Funkcja powinna zwracać element listy o indeksie `index`. Jeśli nie ma takiego elementu, powinna zwracać `None`. 

**uwaga:** zrób to używając obsługi wyjątków.

----

#### Zadanie 2.

Napisz funkcję `divide`, która przyjmie dwa argumenty: `a` i `b`. Muszą być to liczby naturalne. Funkcja ma działać następująco:

* ma sprawdzić, czy `a` i `b` to liczby,
* ma obsłużyć problem dzielenia przez zero.

Oba powyższe przypadki muszą być obsłużone przez wychwytywanie wyjątków.

Jeśli któryś z powyższych warunków nie zostanie spełniony, funkcja ma zwrócić `None`.

#### Zadanie 3.

Napisz funkcję `phone`, która przyjmie parametr `number`, który oznacza numer telefonu. Funkcja ma sprawdzić, czy podany numer znajduje się na liście numerów (wymyśl jakieś). Jeśli nie - musi zwrócić wyjątek typu `Exception` z komentarzem `Nie ma takiego numeru!`.

#### Zadanie 4.

W pliku **exercise4.py** znajdziesz prostą zgadywankę: komputer losuje liczbę od 1 do 10, po czym każe Ci ją zgadnąć. Przeanalizuj kod. Uruchom program. Spróbuj wpisać błędną daną i zobacz, jak w takiej sytuacji zachowuje się program. 

Popraw kod tak, aby po wpisaniu nieprawidłowej wartości nie zakończył działania komunikatem błedu, ale poinformował użytkownika o błędzie i kontynuował działanie. 

*Podpowiedź: Zobacz jaki wyjątek jest zgłaszany i odpowiednio go obsłuż.* 
