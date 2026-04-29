import math
polomer = float(input("zadejte polomer nadoby v metrech: "))
objemkoule = (4/3) * math.pi * (polomer ** 3)
print(f"objem nadoby je priblizne {objemkoule:.2f} mteru krychlovych.")
print(f"Voda vydrzi pro jednoho cloveka na {(objemkoule * 1000) / 5:.2f} dni.") 
