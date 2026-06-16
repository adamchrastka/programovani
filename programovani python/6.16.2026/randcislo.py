print("Zadej rozsah, ve kterém mám hádat číslo:")
print("1 - 1 až 10")
print("2 - 1 až 50")
print("3 - 1 až 100")

volba = int(input("Vyber 1, 2 nebo 3: "))
if volba == 1:
    dolni, horni = 1, 10
elif volba == 2:
    dolni, horni = 1, 50
elif volba == 3:
    dolni, horni = 1, 100
else:
    print("Neplatná volba.")
    exit()
pokusy = 0
print("mysli si cislo")
hadani = (dolni + horni) //2
while dolni <= horni:
    if dolni > horni:
        print("nekozistenti odpovedi bobane")
        break
    print(f"myslim si cislo {hadani}")
    odpoved = input("je to cislo? vetsi = v , mensi = m , spravne = s ): ").strip().lower()
    if odpoved == "v":
        dolni = hadani + 1
    elif odpoved == "m":
        horni = hadani - 1
    elif odpoved == "s":
        print(f"Uhodl jsem cislo! Pocet pokusu: {pokusy}")
        break
    else:
        print("neplatna odpoved. Zadej 'v', 'm' nebo 's'.")
    hadani = (dolni + horni) //2
    pokusy += 1