import numpy as np
from pyquil import Program, get_qc
from pyquil.api import local_forest_runtime


def run_quil(executable, memory_map=None):
    if memory_map is None:
        memory_map = {}
    
    p = Program(executable).wrap_in_numshots_loop(1)
    
    for p_name, p_val in memory_map.items():
        p = p.declare(p_name, "REAL")
        for i, val in enumerate(p_val):
            p += Program(f"RZ({val}) {p_name}[{i}]")
    
    qc = get_qc('qvm', noisy=True)
    
    with local_forest_runtime():
        results = qc.run_and_measure(p, trials=1)
    
    return np.array([results[0]])
