'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math


area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area / 3
tamanho_lata = 18
latas_necessarias = math.ceil(litros_necessarios / tamanho_lata)
preco_lata = 80.0
preco_total = latas_necessarias * preco_lata


print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")
