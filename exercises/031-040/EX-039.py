from datetime import date

print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

birthYear = int(input("Qual seu ano de nascimento? -> "))

currentYear = (date.today().year)

yearsOld = (currentYear - birthYear)

print("----------------------------------------------")

if (yearsOld == 18):
    print("Está no momento de você se alistar!")
elif (yearsOld < 18):
    diffTime = (18 - yearsOld)
    print("Falta(m) {} ano(s) para você se alistar!".format(diffTime))
else:
    diffTime = (yearsOld - 18)
    print("Já passou(aram) {} ano(s) do seu alistamento!".format(diffTime))

print("----------------------------------------------")
print("Encerrando...")
print("----------------------------------------------")
