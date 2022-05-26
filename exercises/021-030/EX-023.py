
print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

number = int(input("Digite um número inteiro entre 0 e 9999 -> "))

unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print("--------------------------")
print("Milhar: {0}".format(thousand))
print("Centena: {0}".format(hundred))
print("Dezena: {0}".format(ten))
print("Unidade: {0}".format(unity))
print("--------------------------")
print("Encerrando...")
print("--------------------------")
