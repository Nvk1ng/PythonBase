'''Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
'''

Fahrenheit = float(input("Digite a temperatura em Fahrenheit:"))
conversao = 5 * ((Fahrenheit-32) / 9)

print(f"{Fahrenheit} Fahrenheit é equivalente a {conversao} graus celsius")