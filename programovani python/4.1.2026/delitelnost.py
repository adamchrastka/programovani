delitelne = []
bubak = []

while len(delitelne) < 10:
    cislo = int(input("Zadejte číslo do listu delitelne: "))
    delitelne.append(cislo)

while len(bubak) < 10:
    cislo = int(input("Zadejte číslo do listu bubak: "))
    bubak.append(cislo)

spolecna_cisla = set(delitelne) & set(bubak)

for hodnota in spolecna_cisla:
    if hodnota == 0:
        delitelne = [x for x in delitelne if x != 0]
    else:
        delitelne = [x for x in delitelne if x % hodnota != 0]

print("Výsledný list delitelne:", delitelne)