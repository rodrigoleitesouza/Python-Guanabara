from random import randint
from time import sleep
from operator import itemgetter

print("---------------------------------------------------")

start = str(input("TECLE ENTER PARA INICIAR O JOGO DE DADOS!"))

print("---------------------------------------------------")

players = {}
ranking = []

players["Player1"] = randint(1, 6)
players["Player2"] = randint(1, 6)
players["Player3"] = randint(1, 6)
players["Player4"] = randint(1, 6)

for key, value in players.items():
    print(f"O {key} tirou o valor {value}.")
    sleep(0.5)

print("---------------------------------------------------")

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

for index, value in enumerate(ranking):
    print(f"{index+1}º lugar: {value[0]} com {value[1]}.")
    sleep(0.5)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
