import random
sutun = 3
setir = 4

A = [[random.randint(1, 10) for _ in range(setir)] for _ in range(sutun)]

print("Matris:")
for sutun in A:
    print(sutun)

cem = 0
for sutun in A:
    maxEded = max(sutun)
    cem += maxEded

print("Hər bir sətrdəki maksimum elementlərin cəmi:", cem)
