'''
desafio035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo.

 "Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre
 maior que a medida do terceiro, então, eles podem formar um triângulo. 
 Por exemplo, dados os segmentos AB = 16 cm, CD = 20 cm e EF = 30 cm,
 é possível usá-los para construir um triângulo, pois as somas abaixo são verdadeiras:

16 + 20 = 36 > 30
16 + 30 = 46 > 20
30 + 20 = 50 > 16" '''
#------------------------------------------------------------------------------------------------------------------------
#código

reta1 = float(input('\nQual o comprimento da primeira reta?\n'))
reta2 = float(input('\nQual o comprimento da segunda reta?\n'))
reta3 = float(input('\nQual o comprimento da terceira reta?\n'))


if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
