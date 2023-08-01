from .graph import graph
import random
import subprocess
import os

class spice:
    def __init__(self, graph, name):
        self.graph = graph
        self.name = name

    def generate(self):
        with open(self.name, "w") as f:
            f.write("*\n")
            f.write("Vvdd vdd 0 5.0\n")
            f.write("Vgnd gnd 0 0.0\n")
            for n in range(1, self.graph.size):
                load = self.graph.loads[n]
                f.write("CL{0} n{0} 0 {1}f\n".format(n, load))

            for r, row in enumerate(self.graph.adj):
                for c, val in enumerate(row[r:]):
                    if val > 0:
                        f.write("R{0}_{1} n{0} n{1} {2}\n".format(r, c, val))

            f.write("Vn0 n0 0 PULSE (0.0 5.0 4.0n 0.5n 0.5n 4.0n 10.0n)\n")
            
            for n in range(1, self.graph.size):
                f.write(".meas tran delay_n{0} TRIG v(n0) VAL=2.5 RISE=1 TD=1.0n TARG v(n{0}) VAL=2.5 RISE=1 TD=1.0n\n".format(n))

            f.write(".TRAN 10p 20.0n 0n 10p\n")
            f.write(".end\n")
    
    def run_sim(self):
        conda = os.environ["OPENRAM_HOME"] + "/../miniconda"
        mpi_exe = conda + "/bin/mpirun"
        xyce_exe = conda + "/bin/Xyce"
        conda_activate = conda + "/bin/activate"
        mpi_cmd = "{} -np 4".format(mpi_exe)
        # Xyce can save a raw file while doing timing, so keep it around
        cmd = "source {3} && {0} {1} -r {2}.raw -o {2}.lis {2} && conda deactivate".format(mpi_cmd,
                                                                                           xyce_exe,
                                                                                           self.name,
                                                                                           conda_activate)
        
        subprocess.run(cmd, shell=True)

