print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

av1 = float(input("Nota AV1: "))
av2 = float(input("Nota AV2: "))

print("---------------------------------------------------")

mean = (av1+av2)/2

if (mean < 5 and mean >= 0):
    print("Média: {} / REPROVADO".format(mean))
elif (mean >= 7 and mean <= 10):
    print("Média: {} / APROVADO".format(mean))
elif (mean == 5 or mean <= 6.9):
    print("Média: {} / RECUPERAÇÃO".format(mean))
else:
    print("Média: {} / ERROR!ERROR!ERROR!ERROR! ".format(mean))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
