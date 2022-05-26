
print("--------------------------")
print("- MANIPULAÇÃO DE STRINGS -")
print("--------------------------")

frase = str(input("Digite a frase que desejar -> ")).upper().strip()

aCount = frase.count("A")
aFindLeft = (frase.find("A")+1)
aFindRight = (frase.rfind("A")+1)

print("--------------------------")
print("A frase digitada possui {0} letra(s) [A].".format(aCount))
print("A posição da 1ª letra [A] encontrada é {0}.".format(aFindLeft))
print("A posição da última letra [A] encontrada é {0}.".format(aFindRight))
print("--------------------------")
print("Encerrando...")
print("--------------------------")
