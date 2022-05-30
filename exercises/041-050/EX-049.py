print("---------------------------------------------------")

number = int(input("Qual número inteiro deseja saber a tabuada? -> "))

print("---------------------------------------------------")

for count in range(1, 10, +1):
    print("{0} x {1} = {2}".format(count, number, number*count))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
