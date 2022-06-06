numberList = []
evenList = []
oddList = []

while (True):
    print("---------------------------------------------------")
    number = (int(input("Digite um número: ")))
    numberList.append(number)

    print("---------------------------------------------------")
    exit = str(input("Gostaria de continuar? [S/N] -> "))

    if exit in "Nn":
        break

for count in range(0, len(numberList), +1):
    if (numberList[count] % 2 == 0):
        evenList.append(numberList[count])
    if (numberList[count] % 2 == 1):
        oddList.append(numberList[count])

print("---------------------------------------------------")

print(f"Lista completa -> {numberList}")

print("---------------------------------------------------")

print(f"Lista de pares -> {evenList}")

print("---------------------------------------------------")

print(f"Lista de ímpares -> {oddList}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
