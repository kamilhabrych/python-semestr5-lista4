napis = str(input("Podaj napis:"))
ilosc = 1

for i in napis:
    if i == " ":
        print()
        ilosc = ilosc + 1
    else:
        print(i, end="")


print()
print("Ilość słów:",ilosc)