print("---------------------------------------------------")

biggestWeight = 0
lowestWeight = 999

for count in range(1, 6, +1):
    weight = int(input("{}º PESSOA / PESO -> ".format(count)))

    if (biggestWeight < weight):
        biggestWeight = weight

    if (lowestWeight > weight):
        lowestWeight = weight

print("---------------------------------------------------")

print("Maior peso -> {0}".format(biggestWeight))
print("Menor peso -> {0}".format(lowestWeight))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
