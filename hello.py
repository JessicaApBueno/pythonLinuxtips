#!/usr/bin/env python3
import os
import sys

__version__ = "0.1.3"
__author__ = "Jessica Bueno"
__license__ = "Unlicense"

arguments = {
    "lang": None,
    "count": None
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
        key = key.lstrip("-").strip() # Limpa traços extras como --lang
        value = value.strip()
        
        if key not in arguments:
            print(f"Invalid Option: {key}")
            sys.exit(1) # Sai com erro se a opção for inválida
            
        arguments[key] = value
    except ValueError:
        print("Erro: Use o formato chave=valor (ex: lang=pt_BR)")
        sys.exit(1)

# Lógica para definir o idioma
current_language = arguments["lang"]
if current_language is None:
    # Pega os 5 primeiros caracteres (ex: pt_BR)
    current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "en_US": "Hello, World!",
}

# Uso do .get() para evitar que o programa quebre caso o idioma não exista no dicionário
print(msg.get(current_language, msg["en_US"]))