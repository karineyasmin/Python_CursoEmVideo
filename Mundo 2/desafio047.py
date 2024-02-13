'''
desafio047
Enunciado:

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

'''
#-----------------------------------------------------------------------------------------------------
#código:
for num in range(1, 51):
    if num % 2 == 0:
        print(f'{num}', end = ' ')
        
#forma que o prof fez:
# for n in range(2, 51, 2):
#     print(n, end = ' ')
# print('Acabou')
        