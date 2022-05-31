print("---------------------------------------------------")

start = int(input("Qual será o primeiro termo da sua PA? -> "))

print("---------------------------------------------------")

index = int(input("Qual a razão da sua PA? -> "))

count = 1

print("---------------------------------------------------")

for start in range(start, start+(10*index), index):
    print("{1}º termo -> {0}...".format(start, count))
    count = count + 1

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
