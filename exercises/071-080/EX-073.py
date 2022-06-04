print("---------------------------------------------------")

count = 0

tuplaLetters = (
    "Real Madrid",
    "Fluminense",
    "Chelsea",
    "Barcelona",
    "Manchester City",
    "Vasco",
    "Flamengo",
    "Cruzeiro",
    "Grêmio",
    "América",
    "Bahia",
    "Espanha",
    "Chapecoense",
    "Nórdico",
    "Holanda",
    "Palmeiras",
    "Qatar",
    "Rodrigo",
    "Texas",
    "Alemanha",
)

for count in range(count, 5, +1):
    print(f"{count+1}º COLOCADO: {tuplaLetters[count]}")

print("---------------------------------------------------")

count = 16

for count in range(count, 20, +1):
    print(f"{count+1}º COLOCADO: {tuplaLetters[count]}")

print("---------------------------------------------------")

print(f"Em ordem alfabética temos: {sorted(tuplaLetters)}")

print("---------------------------------------------------")

print("A posição do time Chapecoense é: {0}".format(
    tuplaLetters.index("Chapecoense")+1))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
