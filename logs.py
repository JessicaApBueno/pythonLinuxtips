#!/usr/bin/env python3

import logging

logging.critical("Deu um erro crítico")
try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("[ERRO] Deu erro %s", str(e))