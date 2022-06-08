from datetime import date

print("---------------------------------------------------")

person = {}

currentYear = (date.today().year)

while(True):
    person["name"] = str(input("Nome: "))

    birthYear = int(input("Qual o ano de nascimento: "))

    person["yearsOld"] = (currentYear - birthYear)

    person["workNumber"] = int(input("Carteira de Trabalho (0 não tem): "))

    if (person["workNumber"] == 0):
        break

    person["jobStarted"] = int(input("Ano de contratação: "))

    person["income"] = float(input("Salário (R$): "))

    person["retirement"] = ((person["jobStarted"] - birthYear) + 35)

    break

print("---------------------------------------------------")

for key, value in person.items():
    print(f"{key} -> {value}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
