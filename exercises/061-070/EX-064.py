print("---------------------------------------------------")

number = 0
count = 0
sum = 0

while(number != 999):
    count = count + 1
    number = float(input("{0}º Número: -> ".format(count)))
    sum = sum + number

print("---------------------------------------------------")

print("Quantidade: {0}".format(count-1))
print("Somatório: {0}".format(sum-999))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
