

team = list()

player = dict()

games = list()


while (True):
    player.clear()
    print("---------------------------------------------------")

    player["name"] = str(input("Qual o nome do jogador? -> "))

    totalGamesPlayed = int(input(f'Quantas partidas {player["name"]} jogou? -> '))

    games.clear()

    print("---------------------------------------------------")

    for count in range(0, totalGamesPlayed):
        games.append(int(input(f'Quantos gols o {player["name"]} marcou na partida {count+1}? -> ')))

    player["goals"] = games[:]
    player["totalGoals"] = sum(games)

    team.append(player.copy())

    while (True):
        print("---------------------------------------------------")
        exit = str(input("Gostaria de adicionar mais um jogador? [S/N] -> ")).upper()[0]
        if exit in "SN":
            break
        if exit not in "SN":
            print("ERROR! Por favor, digite apenas S ou N.")

    if exit == "N":
        break

print("---------------------------------------------------")
print()
print("cód.  ", end="")

for index in player.keys():
    print(f'{index:<15}', end="")
print()

for key, value in enumerate(team):
    print(f'{key:>3}  ', end="")
    for data in value.values():
        print(f'{str(data):<15}', end="")
    print()

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
