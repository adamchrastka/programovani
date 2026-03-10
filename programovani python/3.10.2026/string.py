string = str(input("Zadejte heslo: "))
cislo = 0
if len(string) < 8:
    cislo = cislo + 1  
elif not any(char.isupper() for char in string):
    cislo = cislo + 1
elif not any(char.islower() for char in string):
    cislo = cislo + 1
elif not any(char.isdigit() for char in string):
    cislo = cislo + 1
elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in string):
    cislo = cislo + 1
if cislo == 0:
    print("Heslo je silné.")
elif cislo == 1:
    print("Heslo je střední.")
else:
    print("Heslo je slabé.")