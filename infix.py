import os
import sys
from datetime import datetime

# 1. Captura os argumentos
arguments = sys.argv[1:]
path = os.curdir
# Nome do arquivo de hoje
log_today = f"calculator_log_{datetime.now().strftime('%Y-%m-%d')}.txt"

# 2. Lógica para EXIBIR LOGS
if "--logs" in arguments:
    print("--- Verificando logs existentes ---")
    # Lista todos os arquivos que começam com 'calculator_log'
    arquivos = [f for f in os.listdir(path) if f.startswith("calculator_log")]
    
    if not arquivos:
        print("Nenhum log encontrado.")
    else:
        for arquivo in sorted(arquivos):
            print(f"\n--- Arquivo: {arquivo} ---")
            with open(os.path.join(path, arquivo), "r") as f:
                print(f.read().strip())
    sys.exit(0)

# 3. Lógica da CALCULADORA (executa se não houver argumentos)
if not arguments:
    try:
        operations = input("Enter operations (+, -, *, /): ")
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if operations == "+":
            result = n1 + n2
        elif operations == "-":
            result = n1 - n2      
        elif operations == "*":
            result = n1 * n2
        elif operations == "/":
            if n2 != 0:
                result = n1 / n2
            else:
                print("Error: Division by zero.")
                sys.exit(1)
        else:
            print("Invalid operation.")
            sys.exit(1)

        print(f"Result: {result}")
        
        # Salva o log
        with open(os.path.join(path, log_today), "a") as log_file:
            log_file.write(f"{datetime.now()}: {n1} {operations} {n2} = {result}\n")
            
    except ValueError:
        print("Error: Please enter valid numbers.")
        sys.exit(1)
else:
    print("Usage: python infix.py (to calculate) or python infix.py --logs (to see history)")
    sys.exit(1)