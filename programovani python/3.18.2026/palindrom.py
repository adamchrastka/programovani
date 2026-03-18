# zjistim jestli je to palindrom
slovo = str(input("Zadej slovo: "))
if slovo == slovo[::-1]:
    print("je to palindrom")
else:
    print("neni to palindrom")


slovo1 = str(input("Zadej slovo: "))

slovo3 = ''
for i in range(len(slovo1) - 1, -1, -1):
    slovo3 += slovo1[i]
if slovo1 == slovo3:
    print("je to palindrom")
else:
    print("neni to palindrom")
