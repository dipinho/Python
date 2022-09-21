print("Manipulando uma Lista")
print("Método Index")
# Utilizado para encontrar a posição de um valor especifico
print()

lista = ['Carro', 'Casa', 'Hotel', 'Carro']
pos = lista.index('Casa')

print(f"O item desejado está na posição: {pos}")
print("=========================================")

print("Método Count")
# Retorna o número de vezes que o elemento aparece na lista

lista = ['Carro', 'Casa', 'Hotel', 'Carro']
pos = lista.count('Carro')

print(f'O item desejado aparece: {pos} vezes')
print("=========================================")

print("Método Append")
# Insere um elemento no final da lista

lista = ['Estudando', 'Python']
lista.append('Em casa')
print(lista)
print("=========================================")

print("Método Pop")
# Remove um item 

lista = ['Carro', 'Casa', 'Hotel', 'Carro']
item = lista.pop(2)

print('Item: ',item)
print('Lista: ', lista)
print("=========================================")

print("Método Clear")
# Remove todos os itens da lista

lista1 = ['Carro', 'Casa', 'Hotel', 'Carro']
lista1.clear()

print(lista1)


print("=======================================")