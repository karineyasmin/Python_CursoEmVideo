'''
desafio028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu ou perdeu. '''
#------------------------------------------------------------------------------------------------------------------------
#código

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
    print(f'HAHA, você errou!\nO número em que pensei foi: {numero}')
print('=-='*20)