print("---------------------------------------------------")

estado = {}
brasil = []

for count in range(0, 3, +1):
    estado["UF"] = str(input("Unidade Federativa: -> "))
    estado["SIGLA"] = str(input("Sigla do Estado: -> "))
    print("---------------------------------------------------")

    brasil.append(estado.copy())

for estado in brasil:
    for key, value in estado.items():
        print(f"O campo {key} tem valor {value}.")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
