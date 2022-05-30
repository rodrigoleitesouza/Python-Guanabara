print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

A = float(input("Lado A -> "))
B = float(input("Lado B -> "))
C = float(input("Lado C -> "))

print("--------------------------")

if (A > (((B-C)**2)**0.5) and A < (B+C)):
    solution = "É possivel formar um triângulo!"
else:
    solution = "Não é possível formar um triângulo!"

if (B > (((A-C)**2)**0.5) and B < (A+C)):
    solution = "É possivel formar um triângulo!"
else:
    solution = "Não é possível formar um triângulo!"   

if (C > (((B-A)**2)**0.5) and C < (A+C)):
    solution = "É possivel formar um triângulo!"
else:
    solution = "Não é possível formar um triângulo!"

print("{}".format(solution))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
