from random import randrange

print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")
print("Um número aleatório entre 0 e 5 foi gerado, que tal descobrir?")
print("--------------------------")

randomNumber = randrange(6)

guessNumber = int(input("Digite seu palpite -> "))

print("--------------------------")

if (guessNumber == randomNumber):
    print("Palpite: {0}".format(guessNumber))
    print("Número aleatório: {0}".format(randomNumber))
    print("--------------------------")
    print("Parabéns, você acertou! :D")
else:
    print("Palpite: {0}".format(guessNumber))
    print("Número aleatório: {0}".format(randomNumber))
    print("--------------------------")
    print("Poxa, você errou! :(")

print("--------------------------")
print("Encerrando...")
print("--------------------------")
