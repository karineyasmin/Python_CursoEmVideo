'''
desafio025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. '''
#------------------------------------------------------------------------------------------------------------------------
#código

nome = str(input('Digite seu nome completo: ')).upper().strip()

print('Seu nome tem Silva?', 'SILVA' in nome)