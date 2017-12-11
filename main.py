#!/usr/bin/python3
# main.py
import sys
from conllu.parser import parse_tree
if (len(sys.argv) != 2):
    raise Exception('Invalid Input')
data = parse_tree(open(sys.argv[1], 'r').read())
print(data)
