
print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

name = str(input("Qual o seu nome completo? "))

upperName = name.upper()
lowerName = name.lower()
totalLetters = len(name.replace(" ", ""))
firstName = name.split()

print("--------------------------")
print("Nome maiusculo: {0}".format(upperName))
print("Nome minusculo: {0}".format(lowerName))
print("Total de letras: {0}".format(totalLetters))
print("Qts letras tem o 1° nome: {0}".format(len(firstName[0])))
print("--------------------------")
print("Encerrando...")
print("--------------------------")