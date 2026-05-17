def _classify_arithmetic(self, regs_init, regs_fini, mem_fini, written_regs, read_regs):
    """Classify binary-operation gadgets."""
    operations = {
        'add': 'addition',
        'sub': 'subtraction',
        'mul': 'multiplication',
        'div': 'division',
        'mod': 'modulus',
        'and': 'bitwise AND',
        'or': 'bitwise OR',
        'xor': 'bitwise XOR',
        'not': 'bitwise NOT',
        'shl': 'shift left',
        'shr': 'shift right',
        # add more operations as needed
    }

    # Assuming regs_init and regs_fini are lists of operations
    for op in regs_init + regs_fini:
        if op in operations:
            print(f'Operation {op} is a {operations[op]}')
        else:
            print(f'Operation {op} is not recognized')