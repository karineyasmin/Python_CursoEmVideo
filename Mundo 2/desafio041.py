'''
desafio-041
Enunciado:

A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JUNIOR;
- Até 25 anos: SÊNIOR;
- Acima: MASTER; '''
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#código:
from datetime import date

print('=-' * 23)
print('SISTEMA DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=-' * 23)
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('\nClassificação: MIRIM!')
elif idade <= 14:
    print('\nClassificação: INFANTIL!')
elif idade <= 19:
    print('\nClassificação: JUNIOR!')
elif idade <= 25:
    print('\nClassificação: SÊNIOR!')
else:
    print('\nClassificação: MASTER')
print('=-' * 23)