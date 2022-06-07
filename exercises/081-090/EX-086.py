print("---------------------------------------------------")

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, 3, +1):
    for column in range(0, 3, +1):
        matrix[line][column] = int(input(f"Posição [{line}],[{column}]: "))

print("---------------------------------------------------")

for line in range(0, 3, +1):
    for column in range(0, 3, +1):
        print(f"[{matrix[line][column]}]", end=" ")
    print()

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
