seznam = []
cislo = -1
while cislo != 0:
    cislo = int(input("Zadejte číslo: "))
    if cislo == 0:
        break
    seznam.append(cislo)

print(seznam)