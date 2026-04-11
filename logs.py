#!/usr/bin/env python3
import logging

# 1. Criação do logger customizado
log = logging.Logger("logs.py", logging.WARNING)

# 2. Configuração do Handler (Saída para o console)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 3. Definição do Formato
fnt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(fnt)

# 4. Adiciona o handler ao nosso logger
log.addHandler(ch)


# Use 'log' (sua instância), (o módulo global)
log.debug("Isso é uma mensagem de debug")
log.info("Isso é uma mensagem de informação") 
log.warning("Isso é uma mensagem de aviso")
log.error("Isso é uma mensagem de erro")
log.critical("Deu um erro crítico")

print("-" * 30)

try:
    1 / 0
except ZeroDivisionError as e:
    # Usando o logger customizado aqui também
    log.error("[ERRO] Deu erro %s", str(e))