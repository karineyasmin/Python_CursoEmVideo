''' 
desafio043
Enunciado:

Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostr seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 19.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- mais de 40: Obesidade mórbida; '''
#----------------------------------------------------------------------------------------------------
#código:

print('=-' * 20)
print('\tCalculadora de IMC')
print('=-' * 20)

peso = float(input('Qual é o seu peso (Kg): '))
altura = float(input('Qual é a sua a altura (m): '))
imc = peso / (altura ** 2)

print(f'\nSeu IMC é de {imc:.1f}')

if imc < 18.5:
    print('\nVocê está Abaixo do peso ideal.')
elif imc < 25:
    print('\nVocê está no Peso ideal.')
elif imc < 30:
    print('\nVocê está com Sobrepeso.')
else: 
    print('\nVocê está com Obesidade Mórbida.')
print('=-' * 20)
    
