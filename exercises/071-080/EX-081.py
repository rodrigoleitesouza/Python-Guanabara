numberList = []
fiveAnswer = ""

while (True):
    print("---------------------------------------------------")
    number = (int(input("Digite um número: ")))
    numberList.append(number)

    print("---------------------------------------------------")
    exit = str(input("Gostaria de continuar? [S/N] -> "))

    if exit in "Nn":
        break

numberList.sort(reverse=True)

if 5 in numberList:
    fiveAnswer = "O número 5 está na lista."
else:
    fiveAnswer = "O número 5 não está na lista."

print("---------------------------------------------------")

print(f"Foram digitados {len(numberList)} números.")

print("---------------------------------------------------")

print(f"De forma decrescente -> {numberList}")

print("---------------------------------------------------")

print(fiveAnswer)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
