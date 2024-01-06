'''
desafio018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''
#------------------------------------------------------------------------------------------------------------------------
#código

from math import radians, sin, cos, tan 


angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}') 
cosseno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cosseno::2f}')
tangente = tan(radians(angulo)) 
print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')

