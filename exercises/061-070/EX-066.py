print("---------------------------------------------------")

number = 0
count = 0
sum = 0

while (True):
    count = count + 1
    number = float(input("{0}º Número (999 para parar): -> ".format(count)))

    if (number == 999):
        break

    sum = sum + number

print("---------------------------------------------------")

print("Quantidade: {0}".format(count-1))
print("Somatório: {0}".format(sum))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
