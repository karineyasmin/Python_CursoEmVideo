#desafio032
'''
faça um programa que leia um ano qualquer e mostre se ele é bissexto

"O cálculo é o seguinte:

→  O ano é divisível por 4 quando é possível dividir sua dezena por 4:

2020 = 20 ÷ 4 = 5, ou seja, 2020 é um ano bissexto

Com isso, os próximos anos bissextos divisíveis por 4 serão 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052.

→  E sobre os anos terminados em 00?

400 ÷ 400 = 0 => 400 foi um ano bissexto

500 ÷ 400 = 1,25 => 500 não foi um ano bissexto

Por essa regra, o próximo ano terminado em 00 que será bissexto é 2.400."
'''

#CODIGO:

ano = input('Para saber se um ano é bissexto digite o ano: ').strip
dezena = ano.split()


print(ano[0:2])

