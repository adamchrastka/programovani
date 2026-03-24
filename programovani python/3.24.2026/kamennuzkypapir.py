import random
print("KAMEN NUZKY PAPIR")
kamen = 1
nuzky = 2
papir = 3
hrac = 0
pocitac = 0
remiza = 0

while hrac < 3 and pocitac < 3:
    hrac1 = int(input("Zadej 1 pro kamen, 2 pro nuzky, 3 pro papir: "))
    hrac2 = random.randint(1, 3)
    if hrac1 == hrac2:
        print("remiza")
        remiza += 1
    elif hrac1 == kamen and hrac2 == nuzky or hrac1 == nuzky and hrac2 == papir or hrac1 == papir and hrac2 == kamen:
        print("hrac vyhral")
        hrac += 1
    else:
        print("pocitac vyhral")
        pocitac += 1
print(" ")
print("skore hrace:", hrac)
print("skore pocitace:", pocitac)
print("remizy:", remiza)