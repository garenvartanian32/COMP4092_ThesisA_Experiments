from qiskit import ClassicalRegister, QuantumCircuit, execute

def measure_computational_basis(qc, num_trials):
    '''Measure the state in the computational basis the the given number
    of trials, and return the counts of each output configuration.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to measure.
        num_trials (int): The number of times to run the circuit.
    
    Returns:
        dict: A dictionary containing the counts of each output configuration.
    '''
    cregs = ClassicalRegister(qc.num_qubits, name='c')
    qc.add_register(cregs)
    qc.measure(qc.qregs[0], cregs)
    job = execute(qc, backend='local_qasm_simulator', shots=num_trials)
    results = job.result().get_counts(qc)
    return results
