import os

print("--------------------------")

firstNumber = float(input("1º Número -> "))
secondNumber = float(input("2º Número -> "))

print("--------------------------")

menuOption = 0
biggestNumber = 0

while (menuOption != 5):

    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Trocar números")
    print("[5] Sair do programa")

    print("--------------------------")

    menuOption = int(input("Opção -> "))

    print("--------------------------")

    if (menuOption == 5):
        menuOption = 5
        os.system('cls')

    if (menuOption == 4):
        os.system('cls')
        print("--------------------------")
        firstNumber = float(input("1º Número -> "))
        secondNumber = float(input("2º Número -> "))
        print("--------------------------")

    if (menuOption == 1):
        sum = (firstNumber + secondNumber)
        os.system('cls')
        print("--------------------------")
        print("1º número: {0}".format(firstNumber))
        print("2º número: {0}".format(secondNumber))
        print("--------------------------")
        print("Soma: {0}".format(sum))
        print("--------------------------")

    if (menuOption == 2):
        multiplication = (firstNumber * secondNumber)
        os.system('cls')
        print("--------------------------")
        print("1º número: {0}".format(firstNumber))
        print("2º número: {0}".format(secondNumber))
        print("--------------------------")
        print("Multiplicação: {0}".format(multiplication))
        print("--------------------------")

    if (menuOption == 3):
        if (firstNumber > secondNumber):
            biggestNumber = firstNumber
            os.system('cls')
            print("--------------------------")
            print("1º número: {0}".format(firstNumber))
            print("2º número: {0}".format(secondNumber))
            print("--------------------------")
            print("O maior é o {0} que é o 1º número".format(biggestNumber))
            print("--------------------------")
        else:
            biggestNumber = secondNumber
            os.system('cls')
            print("--------------------------")
            print("1º número: {0}".format(firstNumber))
            print("2º número: {0}".format(secondNumber))
            print("--------------------------")
            print("O maior é o {0} que é o 2º número".format(biggestNumber))
            print("--------------------------")

print("--------------------------")
print("Encerrando...")
print("--------------------------")
