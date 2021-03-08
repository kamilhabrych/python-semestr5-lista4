from math import sqrt

n = int(input("Podaj max zakresu:"))

licznik = 1
mianownik = 1

for mianownik in range(1,n+1):
    mianownik = mianownik + 1
    mianownik = mianownik ** 2
    licznik = licznik + 1/mianownik

print(sqrt(6*licznik))
print(licznik)