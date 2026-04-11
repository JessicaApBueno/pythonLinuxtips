#!/usr/bin/env python3
import logging
import os

# 1. Configuração do Logger
#  DEBUG aqui para que o "funil" deixe passar tudo inicialmente
log = logging.getLogger("logs.py")
log.setLevel(logging.DEBUG)

# 2. Formato das mensagens
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 3. Handler para o Console (Terminal)
#  para mostrar apenas WARNING ou superior no terminal
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch.setFormatter(fmt)
log.addHandler(ch)

# 4. Handler para o Arquivo (Análise posterior)
# O modo 'a' (append) adiciona logs ao final do arquivo sem apagar o anterior
fh = logging.FileHandler("analise.log", mode="a", encoding="utf-8")
fh.setLevel(logging.DEBUG) # No arquivo, queremos todos os detalhes (DEBUG+)
fh.setFormatter(fmt)
log.addHandler(fh)

# --- Testando os logs ---

log.debug("Iniciando o script...") 
log.info("Processamento de dados em andamento.")
log.warning("O uso de memória está subindo.")
log.error("Falha ao conectar em um serviço externo.")
log.critical("O sistema será interrompido!")

print("\n" + "-"*30)
print("Verifique o arquivo 'analise.log' para ver todos os níveis.")
print("-"*30 + "\n")

try:
    1 / 0
except ZeroDivisionError as e:
    # exc_info=True adiciona o traceback completo ao log automaticamente
    log.error("Erro matemático detectado", exc_info=True)