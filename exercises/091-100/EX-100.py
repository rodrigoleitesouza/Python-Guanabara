from random import randint


def randomize(list):
    for count in range(0, 5, +1):
        number = randint(1, 10)
        list.append(number)


def sumEven(list):
    sumEvenNumbers = 0
    for count in range(0, 5, +1):
        if (list[count] % 2 == 0):
            sumEvenNumbers = sumEvenNumbers + list[count]
    return sumEvenNumbers


print("---------------------------------------------------")
start = str(input("            TECLE ENTER PARA INICIAR               "))
print("---------------------------------------------------")


listOfNumbers = []

randomize(listOfNumbers)

result = sumEven(listOfNumbers)

print(f'A lista dos números sorteados é -> {listOfNumbers}')

print("---------------------------------------------------")

print(f'A soma dos números pares da lista acima é -> {result}')

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
