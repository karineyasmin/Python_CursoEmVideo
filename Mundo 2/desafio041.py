'''
desafio-041
Enunciado:

A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JUNIOR;
- Até 20 anos: SÊNIOR;
- Acima: MASTER; '''
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#código:
print('=-' * 23)
print('SISTEMA DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
idade = int(input('\nPara saber sua categoria, digite a sua idade: '))

if idade <= 9:
    print('\nVocê está na categoria MIRIM!')
elif idade <= 14:
    print('\nVocê está na categoria INFANTIL!')
elif idade <= 19:
    print('\nVocê está na categoria JUNIOR!')
elif idade <= 20:
    print('\nVocê está na categoria SÊNIOR!')
else:
    print('\nVocê está na categoria MASTER')