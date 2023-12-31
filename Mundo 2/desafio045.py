''' 
desafio-045
Enunciado:

Crie um programa que faça o computador jogar Jokenpô com você. '''
#-----------------------------------------------------------------------------------------------------
#código:
from random import choice 
from time import sleep # funciona igual sleep do shell Script

print('=-' * 30)
print('**** BEM VINDO(A) AO JOGO DE JOKENPÔ ****')

lista = ['Pedra','Papel', 'Tesoura']

opcoes = print('''Escolha o seu movimento:
                  
                            1 - Pedra
                            2 - Papel
                            3 - Tesoura''')

escolha = int(input(''))
movimento = ' '
if escolha == 1:
    movimento = 'Pedra'
    print('\nVocê escolheu Pedra')
elif escolha == 2:
    movimento = 'Papel'
    print('Você escolheu Papel')
elif escolha == 3:
    movimento = 'Tesoura'
else:
    print('Você só pode escolher Pedra, Papel ou Tesoura')


print('Vamos jogar')
sleep(2)


escolhaPC = choice(lista)
print(escolhaPC)