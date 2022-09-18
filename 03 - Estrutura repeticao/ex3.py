print("Estrutura de Repetição - WHILE")
print()

opcao = -1
while opcao != 0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

print (opcao)