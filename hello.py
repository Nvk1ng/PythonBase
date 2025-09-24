#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente.

como usar: 

Tenha a variavel LANG devidamente configurada exemplo:
    
    export LANG=pt_BR

Execução:

    Python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Matheus Sanderhus"
__license__ = "unlicense"

import os 

current_language = os.getenv("LANG", "en_US")[:5]

# sets (Hash Table) - O(1) - Constante
# dicts (Hash Table) O(1)

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])


""" Ordem de complexidade O(n)

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"
 """