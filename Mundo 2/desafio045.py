''' 
desafio-045
Enunciado:

Crie um programa que faça o computador jogar Jokenpô com você. '''
#-----------------------------------------------------------------------------------------------------
#código:
from random import randint
from time import sleep # funciona igual sleep do shell Script

print('=-' * 30)
print('\t**** BEM VINDO(A) AO JOGO DE JOKENPÔ ****')
print('=-' * 30)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''\t Sua Opções:
         [ 0 ]  -  PEDRA
         [ 1 ]  -  PAPEL
         [ 2 ]  -  TESOURA ''')
jogador = int(input('\nQual é a sua jogada? '))
print('-=' * 11)

#contagem
print('\nVamos jogar...')
print('\n1...')
sleep(1)
print('\n2...')
sleep(1)
print('\n3...')
sleep(2)
print('\nJOKEEEEENPÔ')
sleep(3) 
print('-=' * 11 )

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11 )
#bloco de comparações
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')        
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')        
    else:
        print('Jogada Inválida')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHOU!')        
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')        
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida')
print('-=' * 11 )
        