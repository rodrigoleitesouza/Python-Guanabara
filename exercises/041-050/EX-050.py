print("---------------------------------------------------")

sum = 0

for count in range(1, 7, +1):
    number = int(input("{}º NÚMERO -> ".format(count)))
    if (number % 2 == 0):
        sum = sum + number

print("---------------------------------------------------")

print("A soma dos números pares digitados é {0}.".format(sum))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
