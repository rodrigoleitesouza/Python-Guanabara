import os

print("---------------------------------------------------")

exit = ""
count = 0
sum = 0
biggestNumber = 0
lowestNumber = 999**999

while(exit != "S"):
    count = count + 1
    number = float(input("{0}º Número: -> ".format(count)))
    print("---------------------------------------------------")
    sum = sum + number
    mean = sum/count

    if (biggestNumber < number):
        biggestNumber = number

    if (lowestNumber > number):
        lowestNumber = number

    exit = str(input("Gostaria de encerrar? [S/N] -> ")).upper()
    os.system('cls')

print("---------------------------------------------------")

print(f"Média: {mean:.2f}")
print("Maior: {0}".format(biggestNumber))
print("Menor: {0}".format(lowestNumber))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
