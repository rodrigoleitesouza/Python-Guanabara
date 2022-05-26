
print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

city = str(input("Digite o nome da sua cidade -> "))

splittedCity = city.split()
firstName = splittedCity[0]
solution = firstName=="Santo"

print("--------------------------")
print("O nome da cidade digitada começa com [Santo]? {0}".format(solution))
print("--------------------------")
print("Encerrando...")
print("--------------------------")