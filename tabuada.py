#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
Tabuada do 1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
...
----------------------------------
"""
__version__ = "0.1.0"
__author__ = "Jessica"

numeros = list(range(1, 11))

for numero in numeros:
    print(f"Tabuada do {numero}") 
    for outro_numero in numeros:
        resultado = numero * outro_numero
        print(f"{numero} x {outro_numero} = {resultado}")
    print("-" * 20)
