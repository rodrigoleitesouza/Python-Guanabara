
students = []

while(True):
    print("---------------------------------------------------")
    name = str(input("Nome: "))
    grade1 = float(input("AV1: "))
    grade2 = float(input("AV2: "))
    print("---------------------------------------------------")
    mean = (grade1 + grade2)/2

    students.append([
        name,
        [grade1, grade2],
        mean,
    ])

    exit = str(input("Quer continuar? [S/N] -> "))
    if exit in "Nn":
        break

print("---------------------------------------------------")
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("---------------------------------------------------")

for index, student in enumerate(students):
    print(f'{index:<4}{student[0]:<10}{student[2]:>8.1f}')

while(True):
    print("---------------------------------------------------")
    option = int(input("Mostras as notas de qual aluno? (999 interrompe) -> "))
    if option == 999:
        print("---------------------------------------------------")
        print("Encerrando...")
        print("---------------------------------------------------")
        break
    if (option <= len(students) - 1):
        print(f'As notas de {students[option][0]} são {students[option][1]}')


