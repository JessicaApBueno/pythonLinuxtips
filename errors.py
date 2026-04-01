#!/usr/bin/env python3

import os
import sys

try:
    input("Press Enter to continue...")
    print('The file names.txt exists')
except FileNotFoundError:
    print('The file names.txt does not exist')
    sys.exit(1)

try:
    names = open('names.txt').readlines()
    print(names[2])
except FileNotFoundError:
    print('The file names.txt does not exist')
    sys.exit(1)

if len(names) >= 3:
    print('There are more than 3 names')
else:
    print('There are not more than 3 names')    
    sys.exit(1)
    