import time
slovo = input("Zadej slovo: ")
for i in range (len(slovo)):
    for j in range(10):
        print(slovo[i])
        if j % 10 == 0:
            for k in range(15):
                print(" ")
                print()
        time.sleep(0.5)