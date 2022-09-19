print("Desafio Intermediário - Papagaio poliglota")
print()

while True: 
    try: 
      letra = input() 
      if (letra == 'esquerda'):
        print('ingles')
      elif (letra == 'direita'):
        print('frances')
      elif (letra == 'nenhuma'):
        print('portugues')
      else:
        print('caiu')
    except EOFError: 
        break