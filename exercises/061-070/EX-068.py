from random import randrange

print("---------------------------------------------------")
print("                  PAR ou ÍMPAR                     ")
print("---------------------------------------------------")

victoryCount = 0

while (True):
    computerPlay = randrange(11)
    humanPlay = int(input("Diga seu valor: -> "))
    humanChoice = ""
    computerChoice = ""
    result = ""

    sum = (humanPlay + computerPlay)

    while (humanChoice != "P" and humanChoice != "I"):
        humanChoice = str(input("Par ou Ímpar? [P/I] -> ")).upper()

    if (humanChoice == "P"):
        computerChoice = "I"
    else:
        computerChoice = "P"

    print("---------------------------------------------------")

    print(f"Jogador: {humanPlay}")
    print(f"Computador: {computerPlay}")

    print("---------------------------------------------------")

    print(f"Total: {sum}")

    print("---------------------------------------------------")

    if (sum % 2 == 0):
        result = "PAR"
    else:
        result = "ÍMPAR"

    if (humanChoice == "P" and result == "PAR"):
        print("O jogador venceu! Parabéns! :D")
        print("---------------------------------------------------")
        victoryCount = victoryCount + 1

    elif (humanChoice == "I" and result == "ÍMPAR"):
        print("O jogador venceu! Parabéns! :D")
        print("---------------------------------------------------")
        victoryCount = victoryCount + 1

    elif (humanChoice == "P" and result == "ÍMPAR"):
        print("O computador venceu! Poxa! :(")
        print("---------------------------------------------------")
        print(f"Número de vitórias consecutivas: {victoryCount}")
        break

    elif (humanChoice == "I" and result == "PAR"):
        print("O computador venceu! Poxa! :(")
        print("---------------------------------------------------")
        print(f"Número de vitórias consecutivas: {victoryCount}")
        break

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
