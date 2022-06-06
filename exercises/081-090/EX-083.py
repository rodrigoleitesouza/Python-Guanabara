print("---------------------------------------------------")

expression = str(input("Digite sua expressão -> "))

parenthesisCount = 0

for symbol in expression:
    if symbol == "(":
        parenthesisCount = parenthesisCount + 1
    if symbol == ")":
        parenthesisCount = parenthesisCount - 1

print("---------------------------------------------------")

if (parenthesisCount == 0):
    print("Sua expressão é válida.")
else:
    print("Sua expressão é inválida.")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
