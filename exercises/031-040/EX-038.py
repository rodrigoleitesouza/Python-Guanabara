print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

firstNumber = float(input("1º número: "))
secondNumber = float(input("2º número: "))

print("----------------------------------------------")

if (firstNumber > secondNumber):
    print("O 1º número é maior que o 2º número -> {0} > {1}".format(firstNumber, secondNumber))
elif (firstNumber < secondNumber):
    print("O 2º número é maior que o 1º número -> {1} > {0}".format(firstNumber, secondNumber))
else:
    print("Os números escolhidos são iguais -> {1} = {0}".format(firstNumber, secondNumber))

print("----------------------------------------------")
print("Encerrando...")
print("----------------------------------------------")
