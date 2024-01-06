'''
desafio032
faça um programa que leia um ano qualquer e mostre se ele é bissexto;

"O cálculo é o seguinte:
→  O ano é divisível por 4 quando é possível dividir sua dezena por 4:
2020 = 20 ÷ 4 = 5, ou seja, 2020 é um ano bissexto
Com isso, os próximos anos bissextos divisíveis por 4 serão 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052.

→  E sobre os anos terminados em 00?
400 ÷ 400 = 0 => 400 foi um ano bissexto
500 ÷ 400 = 1,25 => 500 não foi um ano bissexto
Por essa regra, o próximo ano terminado em 00 que será bissexto é 2.400." '''
#------------------------------------------------------------------------------------------------------------------------
#código
from datetime import date

ano = int(input('Que ano quer analisar? Coloque zero para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 5 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')
