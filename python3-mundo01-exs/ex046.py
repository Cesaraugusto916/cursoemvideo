import time

frutas = ["maçã", "banana", "cereja", "pêra", "melancia"]
i = 1
print("\nMinhas frutas favoritas:")
for fruta in frutas:
    print(i*fruta)
    i += 1
    time.sleep(0.6)
