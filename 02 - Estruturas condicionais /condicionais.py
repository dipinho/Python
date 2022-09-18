print("Estrutura Condicional")
print()

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")
    x = saldo - saque
    print("Seu novo saldo é: R$ ",x)

else:
    print("Saldo insuficiente!")