from src.graph import graph
from src.spice import spice

import sys

if len(sys.argv) < 3:
    print("Usage: python gen.py <num_graphs> <num_nodes>")
    exit(-1)

num_graphs = int(sys.argv[1])
num_nodes = int(sys.argv[2])

for n in range(num_graphs):
    g = graph(num_nodes, "g{}".format(n))

    g.generate()
    g.render()

    sp = spice(g, "g{}.sp".format(n))

    sp.generate()
    sp.run_sim()
