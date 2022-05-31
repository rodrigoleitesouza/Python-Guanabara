print("---------------------------------------------------")

number = int(input("Digite um número: "))

primeNumberSum = 0

print("---------------------------------------------------")

for count in range(1, number+1, +1):
    if (number % count == 0):
        primeNumberSum = (primeNumberSum + 1)

if (primeNumberSum != 2):
    print("O número {0} não é primo.".format(number))
else:
    print("O número {0} é primo.".format(number))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
