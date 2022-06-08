print("---------------------------------------------------")

student = {}

student["Nome"] = str(input("Nome: "))
student["Média"] = float(input("Média: "))

print("---------------------------------------------------")

if (student["Média"] >= 7):
    student["Situação"] = "APROVADO"
else:
    student["Situação"] = "REPROVADO"

for key, value in student.items():
    print(f"{key} é igual a {value}.")
    print("---------------------------------------------------")

print("Encerrando...")
print("---------------------------------------------------")
