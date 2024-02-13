'''
desafio049
Enunciado:

Refaça o desafio009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
#----------------------------------------------------------------------------
#código:
print('-='* 20)
print('\t\tTABUADA')
print('-=' * 20)
num = int(input('Digite um número para ver sua tabuada: '))

print(f'A tabuada do número {num} é: ')

for i in range(1,11):
    print(f'{num} x {i:2} = {num * i}')
    