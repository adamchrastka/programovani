print("Kalkulačka")
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
print("Zadej operaci: +, -, *, /, **, //, %")
operace = input("Zadej operaci: ")
match operace:    
    case "+":
        print(f"vysledek: {cislo1 + cislo2}")
    case "-":
        print(f"vysledek: {cislo1 - cislo2}")
    case "*":
        print(f"vysledek: {cislo1 * cislo2}")
    case "/":
        if cislo2 == 0:
            print("nelze delit nulou")
        else:
            print(f"vysledek: {cislo1 / cislo2}")
    case "**":
        print("vysledek: Pouze 1. cislo na druhou")
        print(f"vysledek: {cislo1 * cislo1}")
    case "//":
        if cislo2 == 0:
            print("nelze delit nulou")
        else:            
            print(f"vysledek: {cislo1 // cislo2}")
    case "%":
        if cislo2 == 0:
            print("nelze delit nulou")
        else:            
            print(f"vysledek: {cislo1 % cislo2}")
    case _:
        print("neplatna operace")
