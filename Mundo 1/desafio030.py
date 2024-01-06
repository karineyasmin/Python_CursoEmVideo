'''
desafio030
Crie um programa que leia um número inteiro e mostre na tela se é par ou ímpar. '''
#------------------------------------------------------------------------------------------------------------------------
#código

numero = int(input('Para saber um número é par ou impar, digite um número inteiro:\n'))

if numero % 2 == 0:
    print(f'\nO número é par')
else:
    print('\no número é ímpar')

