''' Enunciado:

Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostr seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 19.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- mais de 40: Obesidade mórbida;'''
#----------------------------------------------------------------------------------------------------
#código
print('=-' * 30)
print('Calculadora de IMC')

peso = float(input('\nDigite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = float(peso / (altura * altura))

print(f'\nSeu IMC é de {imc:.1f}')

if imc < 18.5:
    print('\nVocê está Abaixo do peso')
elif imc < 25:
    print('\nVocê está no Peso ideal')
elif imc < 30:
    print('\nVocê está com Sobrepeso')
else: 
    print('\nVocê está com Obesidade Morbida')
print('=-' * 30)
    
