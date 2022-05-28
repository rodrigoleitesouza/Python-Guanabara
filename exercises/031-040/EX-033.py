print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

number1 = float(input("Digite o 1º número: "))
number2 = float(input("Digite o 2º número: "))
number3 = float(input("Digite o 3º número: "))

biggestNumber = 0
lowestNumber = 0

print("--------------------------")

if (number1 >= number2 and number3):
    biggestNumber = number1

if (number2 >= number1 and number3):
    biggestNumber = number2

if (number3 >= number2 and number1):
    biggestNumber = number3

if (number1 <= number2 and number3):
    lowestNumber = number1

if (number2 <= number1 and number3):
    lowestNumber = number2

if (number3 <= number2 and number1):
    lowestNumber = number3

print("O maior número é -> {0:.2f}".format(biggestNumber))
print("O menor número é -> {0:.2f}".format(lowestNumber))
print("--------------------------")
print("Encerrando...")
print("--------------------------")
