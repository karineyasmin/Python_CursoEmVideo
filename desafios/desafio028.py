#desafio028
'''
Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5,
e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu.
'''

#CODIGO:

import random

numero = random.randrange(0,6)

print('=-='*20)
print('Bem vindo ao jogo da adivinhação!')
print('=-='*20)
print('\nAdivinhe em que numero estou pensando de 0 a 5')

palpite = str(input('\nEm que número estou pensando?\n'))

if palpite == numero:
    print('Parabéns! Você acertou.')
else:
    print(f'HAHA, você errou!\n O número em que pensei foi: {numero}')

print('=-='*20)