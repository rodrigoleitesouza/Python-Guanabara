print("---------------------------------------------------")

numberList = []

biggestNumber = 0
biggestCount = -1
lowestNumber = 999**999
lowestCount = -1

for count in range(0, 5, +1):
    numberList.append(int(input("Digite um número: ")))

    if (numberList[count] > biggestNumber):
        biggestNumber = numberList[count]
        biggestCount = count+1

    if (numberList[count] < lowestNumber):
        lowestNumber = numberList[count]
        lowestCount = count+1


print("---------------------------------------------------")

print(f"Sua lista é -> {numberList}")

print("---------------------------------------------------")

print(f"Maior: {biggestNumber} / Posição: {biggestCount}")

print("---------------------------------------------------")

print(f"Menor: {lowestNumber} / Posição: {lowestCount}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
