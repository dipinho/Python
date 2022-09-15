print("== Operadores de identidade ==")
print()

curso = "Introdução a Python"
nome_curso = curso
saldo, limite = 200, 200

print("curso ocupa a mesma região de memória de nome_curso ?")
print(curso is nome_curso)

print()

print("curso não ocupa a mesma região de memória de nome_curso ?")
print(curso is not nome_curso)

print()
print("saldo ocupa a mesma região de memória de limite ?")
print(saldo is limite)