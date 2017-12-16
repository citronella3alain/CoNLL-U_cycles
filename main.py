#!/usr/bin/python3
# main.py
import sys
from conllu.parser import parse
from graph import Graph

if len(sys.argv) != 2:
    raise Exception('Invalid Input')
data = parse(open(sys.argv[1], 'r').read())
g = Graph(len(data[0])+1)
for word in data[0]:
    g.add_edge(word['head'], word['id'])
if g.is_cyclic():
    print("Cycle found with the following path: {0}".format(g.rec_path))
else:
    print("No cycles found.")
