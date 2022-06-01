print("---------------------------------------------------")

start = int(input("Qual será o primeiro termo da sua PA? -> "))

print("---------------------------------------------------")

index = int(input("Qual a razão da sua PA? -> "))

count = 1

print("---------------------------------------------------")

while (count < 11):
    print("{0}...".format(start))
    start = start + index
    count = count + 1

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
