'''
desafio046

Enunciado:

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício.
Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
#código

from time import sleep
from emoji import emojize

print('\nCONTAGEM REGRESSIVA PARA O ANO NOVO\n')

sleep(1)
for i in range(10, 0, -1):
    print(f'\t\t{i} \n')
    sleep(1)
    
print(emojize(':sparkler::fireworks::sparkler::fireworks: FELIZ ANO NOVO :fireworks::sparkler::fireworks::sparkler:'))
