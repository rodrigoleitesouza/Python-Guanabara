print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

yearsOld = int(input("Idade: "))

print("---------------------------------------------------")

if (yearsOld <= 9):
    print("Classificação: MIRIM")
elif (yearsOld <= 14):
    print("Classificação: INFANTIL")
elif (yearsOld <= 19):
    print("Classificação: JUNIOR")
elif (yearsOld <= 20):
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
