print("---------------------------------------------------")

pessoas = {
    "nome": "Gustavo",
    "sexo": "M",
    "idade": 22,
}

# pessoas["peso"] = 100

# del pessoas["sexo"]

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

print("---------------------------------------------------")

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

print("---------------------------------------------------")

for key, value in pessoas.items():
    print(f"{key} = {value}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
