'''Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, 
usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
'''

gigabytes = int(input("Digite o tamanho do arquivo em gigabytes:"))

conversaoMegabytes = gigabytes * 1024
conversaoKilobytes = gigabytes * 1024 * 1024

print(f"O arquivo tem {conversaoMegabytes} MBs")
print(f"O arquivo tem {conversaoKilobytes} KBs")