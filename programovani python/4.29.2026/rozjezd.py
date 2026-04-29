cislo = 0
cislo = int(input("Zadejte číslo: "))
if cislo > 0:
    print("Číslo je kladné.")
    if cislo % 2 == 0:
        print("Číslo je sudé.")
    elif cislo % 2 != 0:
        print("Číslo je liché.")


    obvod = cislo * 4
    obsah = cislo * cislo
    print(f"Obvod čtverce je {obvod} a obsah čtverce je {obsah}.")
elif cislo < 0:
    cislo = cislo * -1
    print("Číslo je záporné.")
    print(f"cislo je {cislo}")
    print(f"Metry = {cislo} m, milimetry = {cislo * 1000} mm.")

else:
    print("Číslo je nula.")