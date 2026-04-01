#!/usr/bin/env python3

import os
import sys

if os.path.exists('names.txt'):
    input("Press Enter to continue...")
    print('The file names.txt exists')
else:
    print('The file names.txt does not exist')
    sys.exit(1)

names = open('names.txt').readlines()

if len(names) >= 3:
    print('There are more than 3 names')
else:
    print('There are not more than 3 names')    
    sys.exit(1)
    