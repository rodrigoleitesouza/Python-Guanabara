print("---------------------------------------------------")

player = {}

games = []

player["name"] = str(input("Qual o nome do jogador? -> "))

totalGamesPlayed = int(input(f'Quantas partidas {player["name"]} jogou? -> '))

print("---------------------------------------------------")

for count in range(0, totalGamesPlayed):
    games.append(int(input(f'Quantos gols o {player["name"]} marcou na partida {count+1}? -> ')))

player["goals"] = games[:]
player["totalGoals"] = sum(games)

print("---------------------------------------------------")

print(player)

print("---------------------------------------------------")

for key, value in player.items():
    print(f"O campo {key} tem o valor {value}.")

print("---------------------------------------------------")

print(f'O jogador {player["name"]} jogou {len(player["goals"])} partidas.') 

for index, value in enumerate(player["goals"]):
    print(f'  -> Na partida {index+1} fez {value} gols.')

print("---------------------------------------------------")

print(f'No total foram {player["totalGoals"]} gols.')

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
