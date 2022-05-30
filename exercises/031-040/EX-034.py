print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

income = float(input("Digite seu salário -> R$ "))

print("--------------------------")

if (income>=1250):
    newIncome = (income*1.10)
else:
    newIncome = (income*1.15)

print("Seu novo salário é -> R$ {0:.2f}".format(newIncome))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
