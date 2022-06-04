print("---------------------------------------------------")

value = int(input("Qual valor gostaria de sacar? -> "))

bankNote50 = value // 50
rest50 = value % 50

bankNote20 = rest50 // 20
rest20 = rest50 % 20

bankNote10 = rest20 // 10
rest10 = rest20 % 10

bankNote1 = rest10 // 1
rest1 = rest10 % 1

print("---------------------------------------------------")

print(f"Nota de 50: -> {bankNote50}")
print(f"Nota de 20: -> {bankNote20}")
print(f"Nota de 10: -> {bankNote10}")
print(f"Nota de 1: -> {bankNote1}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
