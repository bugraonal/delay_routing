import graphviz
import numpy as np
import random
import sys

class graph:

    def __init__(self, size, name):
        if size <= 1:
            print("Size must be greater than 1")
            exit(-1)
        self.size = size
        self.adj = np.zeros((size, size), dtype=float)
        self.root = 0
        self.name = name

    def generate(self):
        '''
        Will generate a random (for now) graph where every node is connected
        with random weights
        '''
        connected = [0]
        unconnected = [n for n in range(1, self.size)]
        self.loads = [round(random.random(), ndigits=2) for n in range(self.size)]
        while len(unconnected) > 0:
            node = unconnected.pop()
            connectTo = random.choice(connected)
            weight = round(random.random(), ndigits=2)
            self.adj[node][connectTo] = weight
            self.adj[connectTo][node] = weight
            connected.append(node)

    def render(self):
        dot = graphviz.Graph(self.name)
        _ = [dot.node("n" + str(n)) for n in range(self.size)]
        for r, row in enumerate(self.adj):
            for c, val in enumerate(row[r:]):
                if val > 0:
                    dot.edge(str(r), str(c + r), label=str(val))
        dot.render()

if __name__ == "__main__":
    g1 = Graph(int(sys.argv[1]), "g1")
    g1.generate()
    g1.render()
    g2 = Graph(int(sys.argv[1]), "g2")
    g2.generate()
    g2.render()

