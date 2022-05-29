print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

print("Escolha a base de conversão abaixo:")

print("----------------------------------------------")

print("[1] -> binário")
print("[2] -> octal")
print("[3] -> hexadecimal")

print("----------------------------------------------")

choice = int(input("Digite o número correspondete a base desejada -> "))
number = int(input("Qual número deseja converter? -> "))

binNumber = bin(number)[2:]
octNumber = oct(number)[2:]
hexNumber = hex(number)[2:]

print("----------------------------------------------")

if (choice == 1):
    print("O número {0} em binário é {1}.".format(number, binNumber))
elif (choice == 2):
    print("O número {0} em octal é {1}.".format(number, octNumber))
elif (choice == 3):
    print("O número {0} em hexadecimal é {1}.".format(number, hexNumber))
else:
    print("Você escolheu um valor inválido para a base! :(")

print("----------------------------------------------")
print("Encerrando...")
print("------------- ---------------------------------")
