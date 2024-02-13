'''
desafio052
Enunciado:

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
#----------------------------------------------------------------------------------
#código:
print('=*' * 22)
print('\tCalculadora de números primos')
print('=*' * 22)
numero = int(input('Digite um número: ',))
print('')
total = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        print('\033[34m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{i}', end = ' ')
    
print(f'\n\n* Em \033[34m azul\033[m  podemos ver por quais número o {numero} pode ser dividido,')
print(f'* Em \033[31mvermelho\033[m podemos ver por quais números o {numero} não é divisível')
print(f'\n\033[mLogo, o número {numero} foi divisível {total} vezes')

if total == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo, já que um número primo só pode ser divisível por ele mesmo, ou por 1.')
