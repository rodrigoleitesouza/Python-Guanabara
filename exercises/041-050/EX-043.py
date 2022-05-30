print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

weight = float(input("Peso(kg): "))
height = float(input("Altura(m²): "))

bmi = (weight / (height**2))

print("---------------------------------------------------")

if (bmi < 18.5):
    print("IMC: {0:.2f}".format(bmi))
    print("Classificação: ABAIXO DO PESO")
elif (bmi < 25 and bmi >= 18.5):
    print("IMC: {0:.2f}".format(bmi))
    print("Classificação: PESO IDEAL")
elif (bmi < 30 and bmi >= 25):
    print("IMC: {0:.2f}".format(bmi))
    print("Classificação: SOBREPESO")
elif (bmi < 40 and bmi >= 30):
    print("IMC: {0:.2f}".format(bmi))
    print("Classificação: OBESIDADE")
elif (bmi > 40):
    print("IMC: {0:.2f}".format(bmi))
    print("Classificação: OBESIDADE MÓRBIDA")   

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
