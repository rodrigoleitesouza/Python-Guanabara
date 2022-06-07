
peopleList = []

person = []

biggestWeight = lowestWeight = 0

while (True):
    print("---------------------------------------------------")
    person.append(str(input("Nome: ")))
    person.append(float(input("Peso: ")))

    if (len(peopleList) == 0):
        biggestWeight = lowestWeight = person[1]
    else:
        if (person[1] > biggestWeight):
            biggestWeight = person[1]
        if (person[1] < lowestWeight):
            lowestWeight = person[1]

    peopleList.append(person[:])

    person.clear()

    print("---------------------------------------------------")
    exit = str(input("Gostaria de continuar? [S/N] -> "))

    if exit in "Nn":
        break

print("---------------------------------------------------")

print(f"A lista de pessoas cadastradas é -> {peopleList}")

print("---------------------------------------------------")

print(f"Ao todo foram cadastradas {len(peopleList)} pessoas.")

print("---------------------------------------------------")

print(f"Maior peso: {biggestWeight}")

print("---------------------------------------------------")

print(f"Menor peso: {lowestWeight}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
