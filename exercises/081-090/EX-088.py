print("---------------------------------------------------")

from random import randint

numberList = []

games = []

howManyGames = int(input("Quantos jogos deseja sortear? -> "))

totalGames = 1

while (totalGames <= howManyGames):
    count = 0
    while(True):
        number = randint(1, 60)
        if number not in numberList:
            numberList.append(number)
            count = count + 1
        if (count >= 6):
            break

    numberList.sort()

    games.append(numberList[:])

    numberList.clear()

    totalGames = totalGames + 1

print("---------------------------------------------------")

for index, list in enumerate(games):
    print(f"Jogo {index+1}: {list}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
