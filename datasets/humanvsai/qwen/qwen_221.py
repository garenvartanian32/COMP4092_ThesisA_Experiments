def save_matpower(self, fd):
    if not fd:
        raise ValueError('Invalid file descriptor')
    fd.write("mpc.version = '2';\n")
    fd.write('mpc.baseMVA = 100;\n')
    fd.write('mpc.bus = [\n')
    for bus in self.buses:
        fd.write(f'    {bus.bus_i} {bus.type} {bus.Pd} {bus.Qd} {bus.Gs} {bus.Bs} {bus.area} {bus.Vm} {bus.Va} {bus.baseKV} {bus.zone} {bus.Vmax} {bus.Vmin}\n')
    fd.write('];\n')
    fd.write('mpc.gen = [\n')
    for gen in self.generators:
        fd.write(f'    {gen.bus} {gen.Pg} {gen.Qg} {gen.Qmax} {gen.Qmin} {gen.Vg} {gen.mBase} {gen.status} {gen.Pmax} {gen.Pmin} {gen.Pc1} {gen.Pc2} {gen.Qc1min} {gen.Qc1max} {gen.Qc2min} {gen.Qc2max} {gen.ramp_agc} {gen.ramp_10} {gen.ramp_30} {gen.ramp_q} {gen.apf}\n')
    fd.write('];\n')
    fd.write('mpc.branch = [\n')
    for branch in self.branches:
        fd.write(f'    {branch.fbus} {branch.tbus} {branch.r} {branch.x} {branch.b} {branch.rateA} {branch.rateB} {branch.rateC} {branch.ratio} {branch.angle} {branch.status} {branch.angmin} {branch.angmax}\n')
    fd.write('];\n')
    fd.write('mpc.gencost = [\n')