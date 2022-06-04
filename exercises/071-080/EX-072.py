print("---------------------------------------------------")

choice = -1

while (True):
    if (choice > 20 or choice < 0):
        choice = int(input("Digite um número entre 0 e 20 -> "))
        print("---------------------------------------------------")
    else:
        break

tuplaNumbers = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)

print(f"O número {choice} escrito por extenso é {tuplaNumbers[choice]}!")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
