numberList = []

while (True):

    print("---------------------------------------------------")
    number = (int(input("Digite um número: ")))

    if number not in numberList:
        numberList.append(number)
        print("---------------------------------------------------")
        print("Valor adicionado com sucesso!")
    else:
        print("---------------------------------------------------")
        print("Valor duplicado! Tenta novamente!")

    print("---------------------------------------------------")
    exit = str(input("Gostaria de continuar? [S/N] -> "))

    if exit in "Nn":
        break

print("---------------------------------------------------")

numberList.sort()

print(numberList)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
