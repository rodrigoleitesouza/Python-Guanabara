print("---------------------------------------------------")

numberA = int(input("Digite um número: "))
numberB = int(input("Digite um número: "))
numberC = int(input("Digite um número: "))
numberD = int(input("Digite um número: "))

sum = 0
count = 0

tupleNumbers = (
    numberA,
    numberB,
    numberC,
    numberD,
)

print("---------------------------------------------------")

print(f"Você digitou os números: {tupleNumbers}")

print("---------------------------------------------------")

print(f"O número 9 apareceu {tupleNumbers.count(9)} vez(es).")

if (tupleNumbers.count(3) > 0):
    for count in range(0, len(tupleNumbers), +1):
        if (tupleNumbers[count] == 3):
            print("---------------------------------------------------")
            print(
                f"O 1º número 3 apareceu na posição {tupleNumbers.index(3)+1}.")
            break
else:
    print("---------------------------------------------------")
    print("Não existe nenhum número 3 na tupla.")

print("---------------------------------------------------")

for count in range(0, len(tupleNumbers), +1):
    if (tupleNumbers[count] % 2 == 0):
        print("Os números pares digitados são -> ", end="")
        break

for count in range(0, len(tupleNumbers), +1):
    if (tupleNumbers[count] % 2 == 0):
        sum = sum + 1
        print(f"{tupleNumbers[count]}... ", end="")

if (sum == 0):
    print("Nenhum número par foi digitado.")


print("")
print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
