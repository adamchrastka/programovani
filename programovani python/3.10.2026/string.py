string = str(input("Zadejte heslo: "))
if len(string) < 8:
    print("heslo je nejslabsi.")
elif not any(char.isupper() for char in string):
    print("heslo je slabe")
elif not any(char.islower() for char in string):
    print("heslo je min slabe")
elif not any(char.isdigit() for char in string):
    print("heslo je stredne slabe")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in string):
    print("heslo neni slabe")