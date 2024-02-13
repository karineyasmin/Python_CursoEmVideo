'''
desafio054
Enunciado:

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.
'''
#---------------------------------------------------------------------
#código:
from datetime import date
dataAtual = date.today().year
totalMaior = 0
totalMenor = 0
print('')
for pessoa in range (1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = dataAtual - nascimento
    
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print('')
print(f'No total {totalMaior} pessoas são maiores de idade.')
print(f'No total {totalMenor} pessoas são menores de idade.')
