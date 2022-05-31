from datetime import date

print("---------------------------------------------------")

sum = 0

currentYear = (date.today().year)

for count in range(1, 8, +1):
    birthYear = int(input("{}º PESSOA / ANO DE NASCIMENTO -> ".format(count)))

    yearsOld = currentYear - birthYear

    if (yearsOld >= 21):
        sum = sum + 1

print("---------------------------------------------------")

print("Quantidade de pessoa com 21 anos ou mais -> {0}.".format(sum))
print("Quantidade de pessoa com menos de 21 anos ->  {0}.".format(count-sum))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
