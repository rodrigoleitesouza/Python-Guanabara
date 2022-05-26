print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

fullName = str(input("Digite o nome completo desejado -> ")).strip()

arrayNames = fullName.split()

firstName = arrayNames[0]
lastNamePosition = len(arrayNames) - 1
lastName = arrayNames[lastNamePosition]

print("--------------------------")

print("Nome completo: {0}".format(fullName))
print("Primeiro nome: {0}	".format(firstName))
print("Último nome: {0}".format(lastName))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
