def area(width, length):
    area = (width * length)
    return area

print("---------------------------------------------------")

width = float(input("Largura (m): "))
length = float(input("Comprimento (m): "))

print("---------------------------------------------------")

area = area(width, length)

print(f"O terreno com dimensões de {width} x {length} tem área de {area} m².")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
