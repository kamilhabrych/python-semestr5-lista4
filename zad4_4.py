n = int(input("Do jakiego miejsca: "))

for i in range(1,n+1):
    if i == 1:
        logarytm_z_2 = 1
    elif i % 2 == 0:
        logarytm_z_2 = logarytm_z_2 - 1/i
    else:
        logarytm_z_2 = logarytm_z_2 + 1/i

print(logarytm_z_2)

print()

licznik = 1
mianownik = 1

for x in range(1,n+1):
    if x % 2 == 0:
        mianownik = mianownik + 2
        licznik = licznik + 1/mianownik
    else: 
        mianownik = mianownik + 2
        licznik = licznik - 1/mianownik

print(4 * licznik)