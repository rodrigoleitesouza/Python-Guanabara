print("------------------------------------")
print("------ CONDICIONAIS ANINHADAS ------")
print("------------------------------------")

housePrice = float(input("Qual o valor da casa desejada? -> "))
income = float(input("Qual o seu salário? -> "))
yearsToPay = float(input("Em quantos anos deseja pagar? -> "))

totalMonths = (yearsToPay*12)
income30percent = (income*0.30)
monthlyInstallment = housePrice/totalMonths

print("--------------------------")

if (monthlyInstallment > income30percent):
    print("Seu empréstimo foi negado! :(")
else:
    print("Seu empréstimo foi aceito! :D")


print("--------------------------")
print("Encerrando...")
print("--------------------------")
