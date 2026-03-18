cislo = int(input("Zadejte číslo: "))
cislo1 = cislo
faktorial = 1
if cislo < 0:
    print("Faktoriál není definován pro záporná čísla.")
elif cislo == 0:
    print("0! = 1")
else:
    kroky = []
    while cislo > 0:
        faktorial *= cislo
        kroky.append(str(cislo))
        cislo -= 1
    vysledek = " x ".join(kroky)
    print(f"{cislo1}! = {vysledek} = {faktorial}")