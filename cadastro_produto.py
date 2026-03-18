#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 5.00,
    "Id": 478965236,
    "em_estoque": True,
}

cliente = {
    "nome": "Jessica"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

pprint.pprint(f"A cliente {cliente['nome']} comprou {compra['quantidade']}unidades do produto {produto['nome']} nas cores {produto['cores']}")