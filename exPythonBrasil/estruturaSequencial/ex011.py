'''Exercício 11
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''

inteiro1 = int(input("Digite o primeiro numero inteiro:"))
inteiro2 = int(input("Digite o segundo numero inteiro:"))
real = float(input("Digite o numero real:"))

print((inteiro1 * 2) * (inteiro2 / 2))
print((inteiro1 * 3) + real)
print(real ** 3)