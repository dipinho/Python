print("Interpolação de variáveis")
print()

#Existem 3 formas de interpolar variáveis:
	#usando o sinal %
	#Método format
	#f strings


#Método Format
nome = "George"
idade = 33
profissao = "Programador"
linguagem = "Python"

print("Ola, me chamo {3}. Tenho {2} anos, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("=============================================")

PI = 3.14159

print(f"Valor de Pi: {PI:.2f}")
