print("Estrutura de Repetição - WHILE")
print()

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o extrato... ")