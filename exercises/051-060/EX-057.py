print("---------------------------------------------------")

genrer = ""

while (genrer != "M" and genrer != "F"):
    genrer = input("Qual o seu sexo? [F/M] -> ").upper()

    if (genrer != "M" and genrer != "F"):
        print("---------------------------------------------------")
        print("Digite uma resposta válida!")
        print("---------------------------------------------------")

if (genrer == "M"):
    genrer = "Masculino"
elif (genrer == "F"):
    genrer = "Feminino"

print("---------------------------------------------------")

print("Sexo: {0}".format(genrer))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
