def _classify_arithmetic(self, regs_init, regs_fini, mem_fini, written_regs, read_regs):
    classification = {}
    for reg in regs_fini:
        if reg in written_regs:
            if reg in read_regs:
                if regs_fini[reg] != regs_init[reg]:
                    if self._is_arithmetic_operation(regs_init, regs_fini, reg):
                        classification[reg] = 'arithmetic'
                    else:
                        classification[reg] = 'non-arithmetic'
                else:
                    classification[reg] = 'unchanged'
            else:
                classification[reg] = 'written-only'
        else:
            classification[reg] = 'read-only'
    return classification

def _is_arithmetic_operation(self, regs_init, regs_fini, reg):
    """Determine if the change in a register's value is due to an arithmetic operation."""
    initial_value = regs_init[reg]
    final_value = regs_fini[reg]
    if final_value == initial_value + 1 or final_value == initial_value - 1:
        return True
    return False