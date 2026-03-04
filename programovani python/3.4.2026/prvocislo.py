cislo = int(input("Zadej číslo: "))
cislo1 = cislo
prvocislo = 0
for i in range(2, cislo):
    if cislo % i == 0:
        prvocislo = 1
        break
    else:
        prvocislo = 2
if prvocislo == 2:
    print(f"{cislo1} je prvočíslo.")
else:
    print(f"cislo neni prvocislo")


