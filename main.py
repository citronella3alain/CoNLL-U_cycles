#!/usr/bin/python3
# main.py
import sys
if (len(sys.argv) != 2):
    raise Exception('Invalid Input')
filename = sys.argv[1]
fh = open(filename, 'w')

