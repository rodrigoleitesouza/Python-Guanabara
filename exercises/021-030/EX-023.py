
print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

number = str(input("Digite um número entre 0 e 9999 -> "))

unity = number[3]
ten = number[2]
hundred = number[1]
thousand = number[0]

print("--------------------------")
print("Milhar: {0}".format(thousand))
print("Centena: {0}".format(hundred))
print("Dezena: {0}".format(ten))
print("Unidade: {0}".format(unity))
print("--------------------------")
print("Encerrando...")
print("--------------------------")