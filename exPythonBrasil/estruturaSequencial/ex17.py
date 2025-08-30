'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
'''

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))


area_com_folga = area * 1.10


litros_necessarios = area_com_folga / 6


litro_lata = 18
preco_lata = 80.0

litro_galao = 3.6
preco_galao = 25.0

latas_somente = math.ceil(litros_necessarios / litro_lata)
preco_latas_somente = latas_somente * preco_lata

galoes_somente = math.ceil(litros_necessarios / litro_galao)
preco_galoes_somente = galoes_somente * preco_galao

latas_mistura = int(litros_necessarios // litro_lata)
resto_litros = litros_necessarios - (latas_mistura * litro_lata)
galoes_mistura = math.ceil(resto_litros / litro_galao)
preco_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)

print("\n--- Situação 1: Apenas latas de 18 litros ---")
print(f"Quantidade de latas: {latas_somente}")
print(f"Preço total: R$ {preco_latas_somente:.2f}")

print("\n--- Situação 2: Apenas galões de 3,6 litros ---")
print(f"Quantidade de galões: {galoes_somente}")
print(f"Preço total: R$ {preco_galoes_somente:.2f}")

print("\n--- Situação 3: Mistura de latas e galões ---")
print(f"Quantidade de latas: {latas_mistura}")
print(f"Quantidade de galões: {galoes_mistura}")
print(f"Preço total: R$ {preco_mistura:.2f}")
