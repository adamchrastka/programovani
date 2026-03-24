a = 0
b = 0
znaky = ["+", "-", "*", "/"]
def Cisla():
    a = int(input("Zadej první číslo: "))
    b = int(input("Zadej druhé číslo: "))
    return (a, b)
def Operace():
    znak = input("Zadej operaci: ")
    if znak in znaky:
        return znak
    else:
        print("Neplatny znak")
        return Operace()
    
def Soucet(a, b):
    print("Soucet:", a + b)

def Rozdil(a, b):
    print("Rozdil:", a - b)

def Soucin(a, b):
    print("Soucin:", a * b)

def Podil(a, b):
    if b == 0:
        print("nelze delit nulou")
        return None
    else:
        print("Podil:", a / b)

def main():
    if znak == "+":
        Soucet(a, b)
    elif znak == "-":
        Rozdil(a, b)
    elif znak == "*":
        Soucin(a, b)
    elif znak == "/":
        Podil(a, b)
a, b = Cisla()
znak = Operace()
main()