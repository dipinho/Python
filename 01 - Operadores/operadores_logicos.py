print("== Operadores Lógicos ==")
print()

saldo = 1000
saque = 250
limite = 200
conta_especial = True


print("Saldo é maior ou igual que saque?")
print(saldo >= saque)

print()
print("Saque é menor ou igual que limite?")
print(saque<= limite)

print()
print("AND")
print("Saldo é maior que saque e menor que limite?")
print(saldo>= saque and saque <= limite)

print()
print("OR")
print("Saldo é maior que saque e menor que limite?")
print(saldo>= saque or saque <= limite)

print()
print("Exemplo com Parenteses")
print("Saldo é maior que saque e saque é menor que limite, ou conta especial e saldo é maior que saque? ")
print(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

