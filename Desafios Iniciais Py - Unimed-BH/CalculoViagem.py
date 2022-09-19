print("Desafio Inicial - Calculo de Viagem")

valores = input().split()
tempo  = int(valores[0])
velocidade  = int(valores[1])

litro = velocidade / 12
result = tempo * litro

print(f"{result:1.3f}")