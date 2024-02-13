'''
desafio048
Enunciado:

Faça um programa que calcule a soma entre todos os números ímpares que são 
multiplos de três e que se encontram no intervalo de 1 até 500.
'''
#------------------------------------------------------------------------------
#código: 
soma = 0
for num in range(1,501):
    if num % 2 == 1:
        if num % 3 == 0: #se o número for impar:
            soma = soma + num
print('A soma total é: {soma}')
           
           
#outra forma
# soma = 0
# cont = 0
# for c in range (1, 501, 2):
#     if c % 3 == 0:
#         cont += 1
#         soma += c
# print(f'A soma de todos os {cont} valores é {soma}')
