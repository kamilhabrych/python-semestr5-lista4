ile_liczb = int(input("Podaj z ilu liczb obliczyć średnią:"))
suma = 0

for i in range(ile_liczb):
    liczba = int(input("Podaj liczbe: "))
    suma += liczba

srednia = suma / ile_liczb

print()
print(srednia)