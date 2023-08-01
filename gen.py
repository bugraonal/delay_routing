from src.graph import graph
from src.spice import spice

g1 = graph(5, "g1")
g2 = graph(5, "g2")

g1.generate()
g1.render()

g2.generate()
g2.render()

sp1 = spice(g1, "g1.sp")
sp2 = spice(g1, "g1.sp")

sp1.generate()
sp1.run_sim()

sp2.generate()
sp2.run_sim()
