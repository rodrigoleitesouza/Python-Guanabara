print("---------------------------------------------------")

count = 0

totalAdulthood = 0

totalMales = 0

femalesUnder20 = 0


while (True):

    genrer = ""

    exit = ""

    count = count + 1

    yearsOld = int(input(f"{count}º IDADE: "))

    while (genrer != "M" and genrer != "F"):
        genrer = str(input(f"{count}º SEXO [F/M]: ")).upper()

    if (yearsOld > 18):
        totalAdulthood = totalAdulthood + 1

    if (genrer == "M"):
        totalMales = totalMales + 1

    if (genrer == "F" and yearsOld < 20):
        femalesUnder20 = femalesUnder20 + 1

    print("---------------------------------------------------")

    while (exit != "N" and exit != "S"):
        exit = str(input("Gostaria de continuar? [S/N] -> ")).upper()

    if (exit == "N"):
        break

    print("---------------------------------------------------")

print("---------------------------------------------------")

print(f"Pessoas acima de 18 anos -> {totalAdulthood}")
print(f"Quantidade de homens -> {totalMales}")
print(f"Mulheres abaixo de 20 anos -> {femalesUnder20}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
