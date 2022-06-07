print("---------------------------------------------------")

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sumEven = 0

thirdColumnSum = 0

biggestNumberAtSecondLine = 0

for line in range(0, 3, +1):
    for column in range(0, 3, +1):
        matrix[line][column] = int(input(f"Posição [{line}],[{column}]: "))

        if (matrix[line][column] % 2 == 0):
            sumEven = sumEven + matrix[line][column]

        if (column == 2):
            thirdColumnSum = thirdColumnSum + matrix[line][column]

        if (line == 1):
            if (biggestNumberAtSecondLine < matrix[line][column]):
                biggestNumberAtSecondLine = matrix[line][column]

print("---------------------------------------------------")

for line in range(0, 3, +1):
    for column in range(0, 3, +1):
        print(f"[{matrix[line][column]}]", end=" ")
    print()

print("---------------------------------------------------")

print(f"Soma dos pares: {sumEven}")

print("---------------------------------------------------")

print(f"Soma da terceira coluna: {thirdColumnSum}")

print("---------------------------------------------------")

print(f"Maior número na segunda linha: {biggestNumberAtSecondLine}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
