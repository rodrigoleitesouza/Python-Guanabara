from random import randrange

print("---------------------------------------------------")

tuplaRandomNumbers = (
    randrange(100),
    randrange(100),
    randrange(100),
    randrange(100),
    randrange(100),
)

print(f"A tupla com números aleatórios é: {tuplaRandomNumbers}")

print("---------------------------------------------------")

biggestNumber = 0
lowestNumber = 999
count = 0

for count in range(0, len(tuplaRandomNumbers), +1):
    if (biggestNumber < tuplaRandomNumbers[count]):
        biggestNumber = tuplaRandomNumbers[count]
    count = count + 1

count = 0

for count in range(0, len(tuplaRandomNumbers), +1):
    if (lowestNumber > tuplaRandomNumbers[count]):
        lowestNumber = tuplaRandomNumbers[count]
    count = count + 1

print(f"Maior: {biggestNumber}")

print("---------------------------------------------------")

print(f"Menor: {lowestNumber}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
