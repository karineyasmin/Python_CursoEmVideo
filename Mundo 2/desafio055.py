'''
desafio055
Enunciado:

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
#----------------------------------------------------------
#código:

maior = 0
menor = 0

for pessoa in range (1,6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print(f'\no MAIOR peso foi de {maior}Kg')
print(f'\no MENOR peso lido foi de {menor} Kg')
    
    