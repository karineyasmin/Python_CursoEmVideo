'''
desafio051
Enunciado:

Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
#------------------------------------------------------------------------------------------------------------------------------
#código:
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiro + (10 -1) * razao #formula do decimo termo de uma PA

for i in range (primeiro, decimoTermo + razao, razao):
    print(f'{i}', end = ' => ')
print('FIM')

