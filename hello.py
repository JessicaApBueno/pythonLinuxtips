#!/usr/bin/env python3
"""Hello World Multi-language

Depending on the language configured in the environment, the program displays 
the corresponding message.

Usage:

Have the LANG variable properly configured, e.g.:

    export LANG=en_US

Execution:

    python hello.py
    or
    ./hello.py
"""
__version__ = "0.1.1"
__author__ = "Jessica Bueno"
__license__ = "Unlicense"

import os


current_language = os.getenv("LANG", "en_US")[:5]

msg = {
	"pt_BR": "Olá, Mundo!",
	"it_IT": "Ciao, Mondo!",
	"fr_FR": "Bonjour, Monde!",
	"en_US": "Hello, World!",
}

print (msg[current_language])

