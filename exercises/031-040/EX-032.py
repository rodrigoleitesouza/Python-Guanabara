print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

year = int(input("Digite o ano que deseja saber se é bissexto -> "))

print("--------------------------")

if (year % 4 == 0):
    print("O ano de {0} é bissexto.".format(year))
else:
    print("O ano de {0} não é bissexto.".format(year))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
