print("--------------------------")

number = int(input("Digite o número que deseja saber o fatorial -> "))

result = 1
count = 1

while count <= number:
    result = result * count
    count = count + 1

print("--------------------------")

print("Resultado: {0}".format(result))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
