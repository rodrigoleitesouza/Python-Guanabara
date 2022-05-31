print("---------------------------------------------------")

totalYearsOld = 0
oldestManAge = 0
oldestManName = ""
totalFemaleUnder20 = 0

for count in range(1, 6, +1):
    name = str(input("{}º PESSOA / NOME -> ".format(count)))
    yearsOld = int(input("{}º PESSOA / IDADE -> ".format(count)))
    genrer = str(input("{}º PESSOA / SEXO [F/M] -> ".format(count)))

    print("---------------------------------------------------")

    totalYearsOld = totalYearsOld + yearsOld

    if (genrer == "M" and yearsOld > oldestManAge):
        oldestManAge = yearsOld
        oldestManName = name

    if (genrer == "F" and yearsOld < 20):
        totalFemaleUnder20 = totalFemaleUnder20 + 1

yearsOldMean = totalYearsOld/count

print("Média de idade de todas as pessoas -> {0}".format(yearsOldMean))
print("Nome do homem mais velho -> {0}".format(oldestManName))
print("Mulheres com menos de 20 anos -> {0}".format(totalFemaleUnder20))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
