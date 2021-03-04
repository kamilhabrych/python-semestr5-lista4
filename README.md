# Lista 4 - Języki programowania wysokiego poziomu

**Python (4) - Pętle, ciągi znaków i liczby zmiennoprzecinkowe**

(1) Przetestuj kod: for i in ’To jest zdanie’: print(i,end=’*’)
Napisz program w którym użytkownik wprowadza jakieś zdanie. Następnie
to zdanie jest wyświetlone ze spacjami między literami i na końcu podana
jest ilość znaków z zdaniu (łącznie ze spacjami).

(2) Tak jak w (1) wprowadzamy zdanie i dostajemy informację ile jest w
nim literek a (tylko małych). Przetestuj parę razy.

(3) Tak jak w (1) wprowadzamy zdanie. Następnie słowa zdania są wyświetlone osobno w kolejnych linijkach i wreszcie podana jest ilość słów w
zdaniu. (Uwaga: zakładamy, że podane zdanie składa się tylko z liter i spacji).

(4) Następujące równości są prawdziwe:
ln(2) = 1 −
1
2 +
1
3 −
1
4 + ...
π = 4 ∗ (1 −
1
3 +
1
5 −
1
7 + ...)
Napisz program w którym te sumy są liczone do pewnego miesjca (np. do
1000) i sprawdź jak dobrze przybliżają obie liczby. Na ile jest lepszy wynik
biorąc większe sumy np. 10000 ? Dla porównania:
ln(2) ≈ 0.693147 i π ≈ 3.141593

(5) Napisz program liczący średnią. Najpierw użytkownik ma wprowadzić
z ilu liczb chce średnią, a następnie ma wprowadzić te liczby. W końcu ma
być wyliczona i wyświetlona średnia.

(6) Stosując funkcję sqrt (pierwiastek kwadratowy) w modułu math wyświetl pierwiastki liczb naturalnych od 1 do 20. Trzeba użyć:
from math import sqrt
Wyświetl też sinusy liczb od 1 do 20 (funkcja sin jest w module math)
(Uwaga! Zamiast sqrt można też użyć potęgi ** np. 2**0.5 dla √
2)

7) Oblicz sumę:
s = 1 + 1
2
2 +
1
3
2 + ... +
1
1002
Następnie wylicz √
6s i odgadnij czemu jest równe s.
Sprawdź wyliczając s dalej niż do 100 (przetestuj coraz większe wartości.

(8) Niech t=’Ala ma kota’. Stosując print(t[3]), print(t[2:5]) i podobne przykłady odgadnij znaczenie t[i] oraz t[i : j]. Funkcja len() zwraca długość
słowa. Napisz program w którym wprowadzone jest słowo lub zdanie. Następnie zdanie to jest wyświetlone na odwrót, np. dla powyższego t:
atok am alA
1
2

(9) Zero wielomianu x
5 + x + 1 znajduje się w przedziale [-1,0]. Żeby je
znaleźć w przybliżeniu zastosuj w programie następujący algorytm:
1. Niech a=-1 i b=0.
2. Niech c będzie średnią a i b.
3. Jeśli c
5+c+1 ma taki sam znak jak a
5+a+1 to niech a = c w przeciwnym
wypadku niech b = c.
4. Wróć do 2 (wykonaj polecenie 4. dużą ilość razy, np. 100, 1000)
5. Wyświetl c jako przybliżoną wartość zera wielomianu.
6. Wyświetl też c
5 + c + 1 (powinno być bardzo bliskie zera).
