print("Vyberte moznost:")
print("1 - spocitat nohy a hlavy z poctu kraliku a slepic")
print("2 - spocitat pocty kraliku a slepic z poctu nohou a hlav")
volba = input("Zadejte 1 nebo 2: ")

if volba == "1":
    kralici = int(input("Zadejte pocet kraliku: "))
    slepice = int(input("Zadejte pocet slepic: "))
    nohykraliku = kralici * 4
    nohyslepic = slepice * 2
    celkove_nohy = nohykraliku + nohyslepic
    print(f"Celkove pocet nohou kraliku a slepic je: {celkove_nohy}")
    hlavy = kralici + slepice
    print(f"Celkove pocet hlav kraliku a slepic je: {hlavy}")
elif volba == "2":
    hlavy = int(input("Zadejte celkovy pocet hlav: "))
    nohy = int(input("Zadejte celkovy pocet nohou: "))
    kralici = (nohy - 2 * hlavy) // 2
    slepice = hlavy - kralici
    if nohy % 2 != 0 or kralici < 0 or slepice < 0 or 4 * kralici + 2 * slepice != nohy: #proc to tak je 
        print("Neplatny pocet nohou a hlav pro kraliky a slepice.")
    else:
        print(f"Pocet kraliku je: {kralici}")
        print(f"Pocet slepic je: {slepice}")
else:
    print("Neplatna volba. Zadejte 1 nebo 2.")