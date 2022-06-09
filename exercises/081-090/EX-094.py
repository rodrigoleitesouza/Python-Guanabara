listOfPersons = []
person = {}

sum = 0
mean = 0

while (True):
    person.clear()
    print("---------------------------------------------------")
    person["name"] = str(input("Nome: "))

    while (True):
        person["genrer"] = str(input("Sexo [F/M]: ")).upper()[0]
        if (person["genrer"]) in "MF":
            break
        print("ERROR! Por favor, digite apenas F ou M.")

    person["yearsOld"] = int(input("Idade: "))
    sum = sum + person["yearsOld"]
    listOfPersons.append(person.copy())

    while (True):
        print("---------------------------------------------------")
        exit = str(input("Gostaria de adicionar mais uma pessoa? [S/N] -> ")).upper()[0]
        if exit in "SN":
            break
        if exit not in "SN":
            print("ERROR! Por favor, digite apenas S ou N.")

    if exit == "N":
        break

mean = sum / len(listOfPersons)

print("---------------------------------------------------")

print(f"Quantidade de pessoas cadastradas -> {len(listOfPersons)}")

print("---------------------------------------------------")

print(f"Média das idades -> {mean:.2f}")

print("---------------------------------------------------")

print("As mulheres cadastradas são -> ", end="")

for person in listOfPersons:
    if person["genrer"] in "Ff":
        print(f'{person["name"]} ', end="")
print()

print("---------------------------------------------------")

print("As pessoas acima da média de idade são -> ", end="")

for person in listOfPersons:
    if (person["yearsOld"] >= mean):
        print(f'{person["name"]} ', end="")
print()

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
