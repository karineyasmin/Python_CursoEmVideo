#desafio011 - faça um programa que leia a largura e a altura de uma parede  em metros calcule a sua área e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('\nDigite a largura da parede em metros: '))
altura = float(input('\nDigite a altura da parede em metros: '))
areaParede = largura * altura
quantidadeTinta = areaParede / 2 #quantidade que uma lata pinta em metros 

print(f'\nSua parede tem {areaParede}m² de área')
print(f'\nSerão necessários {quantidadeTinta} latas de tinta ')


# 1 lata = 2m² -- 10 / 2