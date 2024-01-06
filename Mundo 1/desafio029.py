'''
desafio029
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$ 7,00 por cada KM acima do limite. '''
#------------------------------------------------------------------------------------------------------------------------
#código

velocidade = int(input('Digite a velocidade: \n'))
limite = 80
multa = (velocidade - limite) * 7

if velocidade > limite:
    print(f'\nVocê foi multado! A velocidade máxima permitida é de 80 Km/h, você estava a {velocidade} KM/h.')
    print(f'Sua multa será de R${float(multa):.2f}')
else: 
    print('\nVocê está dentro do limite de velocidade.')