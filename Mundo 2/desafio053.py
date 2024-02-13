'''
desafio053
Enunciado:

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.

Ex: APOS A SOPA, O LOBO AMA O BOLO, A TORRE DA DERROTA
'''
#----------------------------------------------------------------------------
#código:
frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
tudoJunto = ''.join(palavras)
inverso = tudoJunto[::-1]

'''for letra in range(len(tudoJunto) - 1, -1, -1):
    inverso += tudoJunto[letra]'''
print(f'O inverso de {tudoJunto} é {inverso}')
if inverso == tudoJunto:
    print('A frase é um palíndromo!\n')
else:
    print('A frase não é um palíndromo!\n')
