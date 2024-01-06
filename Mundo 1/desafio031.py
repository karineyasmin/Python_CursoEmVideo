'''
desafio031

Desenvolva um programa que pergunte a distância de uma viagem em Km.

Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200 km 
e R$ 0,45 para viagens mais longas
'''
#------------------------------------------------------------------------------------------------------------------------
#código

distancia = float(input('Qual a distância da viagem em Km ?\n'))

if distancia <= 200:
    print(f'A distância foi de {distancia} KM')
    print(f'Sua passagem custará R${distancia * 0.50:.2f}')
else:
    print(f'\nA distância foi de {distancia} KM')
    print(f'Sua passagem custará R${distancia * 0.45:.2f}')