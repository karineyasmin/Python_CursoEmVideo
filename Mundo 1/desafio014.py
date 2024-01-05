'''
desafio014
Crie um programa que peça ao usuário para digitar a temperatura em °C e converta para °F. '''
#------------------------------------------------------------------------------------------------------------------------
#código

celsius = float(input('Informe a temperatura em °C: '))
faren = ((9 * celsius) / 5) + 32

print(f'A temperatura de {celsius}°C corresponde a {faren}°F!')