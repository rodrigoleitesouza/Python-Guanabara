from random import randrange

print("--------------------------")
print("Um número aleatório entre 1 e 10 foi gerado, que tal descobrir?")
print("--------------------------")

randomNumber = randrange(10)+1

guessNumber = 99

guessCount = 0

while (guessNumber != randomNumber):
    guessNumber = int(input("Digite seu palpite -> "))
    print("--------------------------")

    guessCount = guessCount + 1

    if (guessNumber == randomNumber):
        print("Número aleatório: {0}".format(randomNumber))
        print("Palpite: {0}".format(guessNumber))
        print("Número de palpites: {0}".format(guessCount))
        print("--------------------------")
        print("Parabéns, você acertou! :D")
    else:
        print("Poxa, você errou! Tente outro número!")
        print("--------------------------")

print("--------------------------")
print("Encerrando...")
print("--------------------------")
