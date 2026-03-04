cislo = int(input("Zadej číslo: ")) # prvni cislo
druhycislo = int(input("Zadej číslo: ")) # druhe cislo
if druhycislo > cislo:
    for i in range(cislo, druhycislo + 1):
        prvocislo = True
        if i < 2:
            prvocislo = False
        else:
            for j in range(2, i):
                if i % j == 0:
                    prvocislo = False
                    break
        if prvocislo:
            print(f"{i} je prvočíslo.")





