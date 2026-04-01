# min a max a rozdil
def minamax(seznam):
    if not seznam:
        return None, None

    min_hodnota = seznam[0]
    max_hodnota = seznam[0]

    for cislo in seznam[1:]:
        if cislo < min_hodnota:
            min_hodnota = cislo
        if cislo > max_hodnota:
            max_hodnota = cislo

    return min_hodnota, max_hodnota
def spocitej_rozdil(min_hodnota, max_hodnota):
    return max_hodnota - min_hodnota
def main():
    seznam = []

    print("Zadejte čísla, pro ukončení zadejte 0")
    cislo = -1
    while cislo != 0:
        cislo = int(input("Zadejte číslo: "))
        if cislo == 0:
            break
        seznam.append(cislo)

    min_hodnota, max_hodnota = minamax(seznam)
    if min_hodnota is None:
        print("Nezadali jste žádné číslo.")
        return

    rozd = spocitej_rozdil(min_hodnota, max_hodnota)
    print(f"Min: {min_hodnota}, Max: {max_hodnota}, Rozdíl: {rozd}")
main()