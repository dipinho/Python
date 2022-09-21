print("Fatiando uma Lista")
print()

# lista[ inicio : fim : passo ]

lista = [10, 20, 30, 40, 50, 60]

print(lista[2:5])

print("=========================")
print("Percorrendo uma Lista")
print()

lista = [10, 20, 30, 40, 50, 60]

for num in lista:
    print(num)

print()
print("=========================")
print("Percorrendo uma Lista com Enumerate")
print()

lista = [10, 20, 30, 40, 50, 60]

for indice, valor in enumerate(lista):
    print(f"indice={indice}, valor={valor}")

